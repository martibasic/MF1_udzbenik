"""Reject corrupted observations and unsupported claims about the experimental case."""
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from verify_backstep_data import validate_case, validate_notebook

SOURCE = Path(__file__).resolve().parents[1] / 'data/cfd/backstep_experiment'


class ExperimentalReferenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.case = Path(self.temp.name) / 'case'
        shutil.copytree(SOURCE, self.case)

    def change_json(self, name, change):
        path = self.case / name
        data = json.loads(path.read_text(encoding='utf-8'))
        change(data)
        path.write_text(json.dumps(data), encoding='utf-8')

    def test_primary_data_pass(self):
        self.assertEqual(validate_case(self.case), [])

    def test_modified_measurement_fails(self):
        path = self.case / 'comparison.csv'
        path.write_text(path.read_text().replace('-0.00022', '-0.00023'))
        self.assertTrue(any('primary archive' in x for x in validate_case(self.case)))

    def test_modified_unselected_archive_row_fails(self):
        path = self.case / 'sources/cf.exp.dat'
        path.write_text(path.read_text().replace('2.88e-3', '2.89e-3'))
        self.assertTrue(any('changed primary archive' in x for x in validate_case(self.case)))

    def test_invented_confidence_level_fails(self):
        self.change_json('uncertainty.json', lambda d: d.update(coverage_probability=0.95))
        self.assertTrue(any('uncertainty' in x for x in validate_case(self.case)))

    def test_unsupported_convergence_fails(self):
        self.change_json('case.json', lambda d: d['cfd'].update(grid_convergence_established=True))
        self.assertTrue(any('convergence claim' in x for x in validate_case(self.case)))

    def test_wrong_conditions_fail(self):
        self.change_json('case.json', lambda d: d['conditions'].update(Re_H=50000))
        self.assertTrue(any('flow conditions' in x for x in validate_case(self.case)))

    def test_notebook_source_drift_fails(self):
        original = SOURCE.parents[2] / 'notebooks/u12_poiseuille_konvergencija.ipynb'
        self.assertEqual(validate_notebook(original, self.case), [])
        notebook = self.case / 'changed.ipynb'
        notebook.write_text(original.read_text(encoding='utf-8').replace('5.882, -0.00022', '5.882, -0.00023'),
                            encoding='utf-8')
        self.assertTrue(any('disagrees' in x for x in validate_notebook(notebook, self.case)))


if __name__ == '__main__':
    unittest.main()
