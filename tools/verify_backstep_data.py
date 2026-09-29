"""Check the public experimental/CFD archive without inventing validation evidence."""
from __future__ import annotations

import csv
import ast
import hashlib
import json
import math
from pathlib import Path


ARCHIVE_HASHES = {
    'cf.exp.dat': 'cd9b6434b7956bc58e859de6af654cd7f891e25303babf1dd8633d6c58f74276',
    'backstep_cfl3d_cf_sst.dat': '04709a5572afd5d8141af11082ed0e36abef00b4aed574ea4cef4244cb4c7a5c',
    'profiles.exp.dat': '23e8b44db52bfc36c66af6b743a4080c34f0165eb213a3db29c0914e12cf598d',
}


def numeric_rows(path: Path, columns: int) -> list[list[float]]:
    result = []
    for line in path.read_text(encoding='utf-8').splitlines():
        if not line.strip() or line.startswith(('#', 'variables=', 'zone')):
            continue
        values = list(map(float, line.split()))
        if len(values) != columns or not all(math.isfinite(x) for x in values):
            raise ValueError(f'{path.name}: invalid numeric row')
        result.append(values)
    return result


def validate_case(folder: Path) -> list[str]:
    issues = []

    def require(condition, message):
        if not condition:
            issues.append('backstep_experiment: ' + message)

    try:
        case = json.loads((folder / 'case.json').read_text(encoding='utf-8'))
        uncertainty = json.loads((folder / 'uncertainty.json').read_text(encoding='utf-8'))
        provenance = json.loads((folder / 'provenance.json').read_text(encoding='utf-8'))
        declared = {Path(a['file']).name: a for a in provenance['archives']}
        require(set(declared) == set(ARCHIVE_HASHES), 'incomplete source archive inventory')
        for name, expected in ARCHIVE_HASHES.items():
            data = (folder / 'sources' / name).read_text(encoding='utf-8').encode('utf-8')
            require(hashlib.sha256(data).hexdigest() == expected, f'changed primary archive {name}')
            require(declared[name]['sha256_lf'] == expected, f'changed provenance hash {name}')
            require(declared[name]['url'] == 'https://tmbwg.github.io/turbmodels/Backstep_validation/' + name,
                    f'wrong primary source URL {name}')
        require(case['data_classification'] == 'public_experiment_and_published_cfd'
                and provenance['external_measurements_used'] is True,
                'experimental observations must remain distinct from constructed data')
        require(case['conditions'] == {'Re_H': 36000, 'Mach': 0.128, 'roof_angle_deg': 0,
                                       'reference_velocity_station_x_over_H': -4},
                'wrong flow conditions or normalization')
        experiment = case['experiment']
        require(experiment['reattachment_x_over_H'] == 6.26
                and experiment['reported_half_width'] == 0.10,
                'wrong published experimental reattachment range')
        require(experiment['confidence_level'] is None
                and uncertainty['reported_interval_is_standard_uncertainty'] is False
                and uncertainty['coverage_probability'] is None
                and uncertainty['combined_validation_uncertainty'] is None,
                'the reported range is not a standard or combined validation uncertainty')
        require(uncertainty['reported_reattachment_interval'] == [6.16, 6.36],
                'wrong reported experimental interval')
        require(case['cfd']['code'] == 'CFL3D' and case['cfd']['model'] == 'SSTm'
                and case['cfd']['time_description'] == 'quasi-steady',
                'wrong CFD code, model variant or time description')
        require(case['cfd']['local_simulation_performed'] is False
                and case['cfd']['grid_convergence_established'] is False,
                'unsupported simulation or convergence claim')
        measurements = numeric_rows(folder / 'sources/cf.exp.dat', 3)
        computed = numeric_rows(folder / 'sources/backstep_cfl3d_cf_sst.dat', 2)
        require(len(measurements) == 20 and len(computed) == 860, 'incomplete numeric archives')
        with (folder / 'comparison.csv').open(encoding='utf-8', newline='') as handle:
            selected = list(csv.DictReader(handle))
        require(len(selected) == 4, 'comparison must contain exactly four original rows')
        for series, archive in [('experiment', measurements), ('cfl3d_sstm', computed)]:
            chosen = [r for r in selected if r['series'] == series]
            require(len(chosen) == 2, f'{series}: two endpoints required')
            coordinates = []
            for row in chosen:
                values = [float(row['x_over_H']), float(row['Cf'])]
                if series == 'experiment':
                    values.append(float(row['reported_Cf_error']))
                else:
                    require(row['reported_Cf_error'] == '', 'no experimental error for CFD rows')
                require(values in archive, f'{series}: row is not from the stated primary archive')
                coordinates.append(values)
            if len(coordinates) == 2:
                a, b = coordinates
                require(5 < a[0] < b[0] < 8 and a[1] < 0 < b[1],
                        f'{series}: wrong downstream reattachment bracket')
        require({r['series'] for r in selected} == {'experiment', 'cfl3d_sstm'},
                'unknown series or swapped provenance')
    except (OSError, ValueError, KeyError, TypeError) as error:
        issues.append(f'backstep_experiment: unreadable/incomplete data: {error}')
    return issues


def validate_notebook(notebook: Path, folder: Path) -> list[str]:
    """The standalone notebook must embed exactly the same four source rows."""
    try:
        book = json.loads(notebook.read_text(encoding='utf-8'))
        cells = [c for c in book['cells'] if c.get('id') == 'backstep-experiment-calculation']
        if len(cells) != 1:
            return ['backstep_experiment: missing or duplicated notebook calculation']
        tree = ast.parse(''.join(cells[0]['source']))
        values = {node.targets[0].id: ast.literal_eval(node.value) for node in tree.body
                  if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name)
                  and node.targets[0].id in {'backstep_experiment', 'backstep_cfd'}}
        with (folder / 'comparison.csv').open(encoding='utf-8', newline='') as handle:
            rows = list(csv.DictReader(handle))
        for variable, series in [('backstep_experiment', 'experiment'), ('backstep_cfd', 'cfl3d_sstm')]:
            expected = [(float(r['x_over_H']), float(r['Cf'])) for r in rows if r['series'] == series]
            if values.get(variable) != expected:
                return [f'backstep_experiment: notebook {variable} disagrees with source rows']
    except (OSError, ValueError, KeyError, TypeError, SyntaxError) as error:
        return [f'backstep_experiment: cannot check notebook: {error}']
    return []
