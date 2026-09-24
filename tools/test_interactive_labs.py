"""Neovisne fizikalne regresije i ponašanje triju samostalnih laboratorija."""
from contextlib import redirect_stdout
import io
import json
import linecache
import os
from pathlib import Path
import tempfile
import unittest

os.environ.setdefault("MPLBACKEND", "Agg")
import numpy as np
import matplotlib.pyplot as plt

from execute_notebooks import INTERACTIVE_LABS, NOTEBOOK_DIR, validate_notebook


def load_lab(lab_id, ui=False):
    name = next(name for name, value in INTERACTIVE_LABS.items() if value == lab_id)
    notebook = json.loads((NOTEBOOK_DIR/name).read_text(encoding="utf8"))
    scope = {"__name__": "__mf1_lab_test__"}
    tags = {"mf1-lab-model", "mf1-lab-common", "mf1-lab-ui"} if ui else {"mf1-lab-model"}
    with redirect_stdout(io.StringIO()):
        for cell in notebook["cells"]:
            if tags.intersection(cell.get("metadata", {}).get("tags", [])):
                source = "".join(cell["source"])
                filename = f"{name}#{cell['id']}"
                linecache.cache[filename] = (len(source), None, source.splitlines(True), filename)
                exec(compile(source, filename, "exec"), scope)
    return scope


class Physics(unittest.TestCase):
    def test_rotation_reference_and_scaling(self):
        state = load_lab("rotation")["rotation_state"]
        s = state(omega=7, R=.55, h0=.7, H=1.4)
        self.assertAlmostEqual(s["z0"], .3222604485219164)
        self.assertAlmostEqual(s["zR"], 1.0777395514780836)
        self.assertLess(abs(s["volume"]/s["volume_ref"]-1), 3e-6)
        a, b = state(omega=2), state(omega=4)
        self.assertAlmostEqual((b["zR"]-b["z0"])/(a["zR"]-a["z0"]), 4)
        self.assertEqual(state(omega=0)["z0"], .7)

    def test_rotation_first_event_and_no_fictitious_volume(self):
        state = load_lab("rotation")["rotation_state"]
        dry = state(omega=10, h0=.3, H=1.4)
        spill = state(omega=10, h0=.9, H=1.4)
        self.assertEqual(dry["first"], "dodir dna")
        self.assertEqual(spill["first"], "prelijevanje")
        self.assertIsNone(dry["volume"])
        self.assertEqual(spill["status"], "limit")
        boundary = state(omega=0, h0=1., H=1.)
        self.assertEqual(boundary["status"], "ok")
        self.assertEqual(state(omega=.1, h0=1., H=1.)["status"], "limit")

    def test_rotation_invalid_input(self):
        state = load_lab("rotation")["rotation_state"]
        for values in [dict(R=0), dict(h0=2, H=1), dict(omega=-1), dict(H=np.nan)]:
            with self.assertRaises(ValueError):
                state(**values)

    def test_venturi_published_oil_and_calibration(self):
        state = load_lab("venturi")["venturi_state"]
        s = state()
        self.assertAlmostEqual(s["Q"]*1000, 5.2479185043, places=9)
        self.assertAlmostEqual(s["dp_ideal"], 22478.634)
        corrected = state(Cd=.9)
        self.assertAlmostEqual(corrected["Q"]/s["Q"], .9)
        self.assertAlmostEqual(corrected["dp_ideal"]/corrected["dp"], .81)
        self.assertEqual(state(dp_kPa=0)["Q"], 0)

    def test_venturi_uncertainty_against_central_differences(self):
        state = load_lab("venturi")["venturi_state"]
        base = dict(D1_mm=80, D2_mm=40, dp_kPa=18, rho=998, Cd=.985)
        s = state(**base, uD2_pct=.25, udp_pct=.5, uCd_pct=.3)
        variance = 0
        for key, rel in [("D2_mm", .0025), ("dp_kPa", .005), ("Cd", .003)]:
            step = base[key]*1e-5
            derivative = (state(**{**base, key: base[key]+step})["Q"]
                          - state(**{**base, key: base[key]-step})["Q"])/(2*step)
            variance += (derivative*base[key]*rel)**2
        self.assertAlmostEqual(s["uQ"]/np.sqrt(variance), 1., places=8)

    def test_venturi_invalid_inputs(self):
        state = load_lab("venturi")["venturi_state"]
        for values in [dict(D2_mm=60), dict(rho=0), dict(Cd=0), dict(dp_kPa=-1),
                       dict(Cd=np.inf), dict(uD2_pct=-1)]:
            with self.assertRaises(ValueError):
                state(**values)

    def test_fv_convergence_and_independent_exact_profile(self):
        solve = load_lab("poiseuille")["poiseuille_fv"]
        errors = []
        for n in [8, 16, 32, 64]:
            # Izbor daje u = 0,025(1-r²/R²), Q = pi*1,25e-8.
            s = solve(radius=.001, delta_p=100., mu=.001, length=1., n=n)
            exact = .025*(1-(s["r"]/.001)**2)
            errors.append(np.max(np.abs(s["u"]-exact)))
            self.assertLess(s["residual"], 1e-10)
            self.assertLess(abs(s["pressure_force"]+s["wall_force"]), 1e-12)
            self.assertGreater(s["Q"], np.pi*1.25e-8)
            self.assertLess(abs(s["Q"]/(np.pi*1.25e-8)-1), .017)
        np.testing.assert_allclose(np.array(errors[:-1])/errors[1:], 4, rtol=1e-8)

    def test_fv_zero_and_physical_scaling(self):
        solve = load_lab("poiseuille")["poiseuille_fv"]
        zero = solve(delta_p=0)
        self.assertTrue(np.all(zero["u"] == 0))
        self.assertEqual(zero["residual"], 0)
        nominal, double_mu, double_dp = solve(), solve(mu=2.004e-3), solve(delta_p=4.008)
        self.assertAlmostEqual(double_mu["Q"]/nominal["Q"], .5)
        self.assertAlmostEqual(double_dp["Q"]/nominal["Q"], 2.)
        self.assertEqual(solve(radius=.015, delta_p=6)["status"], "limit")

    def test_fv_invalid_inputs(self):
        solve = load_lab("poiseuille")["poiseuille_fv"]
        for values in [dict(n=0), dict(n=8.5), dict(radius=-1), dict(mu=0), dict(delta_p=np.nan)]:
            with self.assertRaises(ValueError):
                solve(**values)


class Interface(unittest.TestCase):
    def test_controls_comparison_reset_and_invalid_result(self):
        with redirect_stdout(io.StringIO()):
            for lab_id, key, changed in [("rotation", "omega", 8.),
                                          ("venturi", "D2_mm", 35.),
                                          ("poiseuille", "n", 32)]:
                with self.subTest(lab=lab_id):
                    lab = load_lab(lab_id, ui=True)["mf1_lab"]
                    initial = lab["controls"][key].value
                    lab["save"].click()
                    lab["controls"][key].value = changed
                    self.assertEqual(lab["state"]["reference"][key], initial)
                    self.assertIsNotNone(lab["state"]["result"])
                    lab["reset"].click()
                    self.assertEqual(lab["controls"][key].value, initial)
                    self.assertIsNone(lab["state"]["reference"])
                    lab["root"].close()
            lab = load_lab("venturi", ui=True)["mf1_lab"]
            lab["controls"]["D2_mm"].value = 90
            self.assertIsNone(lab["state"]["result"])
            self.assertTrue(lab["save"].disabled)
            lab["preset"].value = 'Voda — zasebni nastavni slučaj'
            self.assertIsNotNone(lab["state"]["result"])
            self.assertEqual(lab["controls"]["D1_mm"].value, 80.)
            lab["root"].close()
        plt.close('all')

    def test_notebooks_remain_standalone_and_common_ui_agrees(self):
        common = []
        for name in INTERACTIVE_LABS:
            path = NOTEBOOK_DIR/name
            self.assertEqual(validate_notebook(path), [])
            notebook = json.loads(path.read_text(encoding='utf8'))
            common.append(next(''.join(c['source']) for c in notebook['cells']
                               if 'mf1-lab-common' in c.get('metadata', {}).get('tags', [])))
        self.assertEqual(len(set(common)), 1)

    def test_validator_keeps_dependency_boundary(self):
        name = next(iter(INTERACTIVE_LABS))
        notebook = json.loads((NOTEBOOK_DIR/name).read_text(encoding='utf8'))
        code = next(c for c in notebook['cells'] if c['cell_type']=='code')
        code['source'] = ''.join(code['source']) + '\nimport scipy\n'
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/name
            path.write_text(json.dumps(notebook), encoding='utf8')
            self.assertTrue(any('scipy' in issue for issue in validate_notebook(path)))


if __name__ == '__main__':
    unittest.main()
