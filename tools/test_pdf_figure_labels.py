"""Regressions for actual PDF labels and canonical figure numbering."""
import unittest

import pymupdf

from audit_pdf import _figure_numbering_issues
from audit_pdf_layout import figure_font_issues, figure_label_issues, _normalise_label


class FigureLabelTests(unittest.TestCase):
    def document(self, pages):
        document = pymupdf.open()
        self.addCleanup(document.close)
        for rows in pages:
            page = document.new_page(width=595.276, height=841.89)
            for y, text, size in rows:
                page.insert_text((75, y), text, fontsize=size)
        return document

    def test_small_figure_with_all_labels_passes(self):
        document = self.document([[(100, 'fluid', 9.5), (130, 'h', 9),
                                   (160, 'Slika 1.1: Tank', 9.5)]])
        self.assertEqual(figure_label_issues(document, {'1.1': ['fluid', 'h']}), [])
        self.assertEqual(figure_font_issues(document), [])

    def test_missing_label_fails(self):
        document = self.document([[(100, 'fluid', 9.5), (160, 'Slika 1.1: Tank', 9.5)]])
        issues = figure_label_issues(document, {'1.1': ['fluid', 'h']})
        self.assertEqual(len(issues), 1)
        self.assertIn("['h']", issues[0])

    def test_duplicate_labels_need_separate_occurrences(self):
        document = self.document([[(100, 'h', 9), (160, 'Slika 1.1: Tank', 9.5)]])
        self.assertTrue(figure_label_issues(document, {'1.1': ['h', 'h']}))

    def test_label_cannot_come_from_another_figure(self):
        document = self.document([[(100, 'Slika 1.1: First', 9.5), (140, 'fluid', 9),
                                   (180, 'Slika 1.2: Second', 9.5)]])
        issues = figure_label_issues(document, {'1.1': ['fluid'], '1.2': ['fluid']})
        self.assertEqual(len(issues), 1)
        self.assertIn('slika 1.1', issues[0])

    def test_rows_may_span_pages(self):
        document = self.document([[(100, 'h', 9)],
                                  [(100, 'h', 9), (140, 'Slika 1.1: Two rows', 9.5)]])
        self.assertEqual(figure_label_issues(document, {'1.1': ['h', 'h']}), [])

    def test_small_font_fails_both_checks(self):
        document = self.document([[(100, 'fluid', 8), (160, 'Slika 1.1: Tank', 9.5)]])
        self.assertTrue(figure_label_issues(document, {'1.1': ['fluid']}))
        self.assertTrue(figure_font_issues(document))

    def test_body_text_and_running_header_cannot_supply_label(self):
        document = self.document([[(30, 'header', 9), (100, 'body', 11),
                                   (160, 'Slika 1.1: Tank', 9.5)]])
        issues = figure_label_issues(document, {'1.1': ['header', 'body']})
        self.assertEqual(len(issues), 1)
        self.assertIn('header', issues[0])
        self.assertIn('body', issues[0])

    def test_missing_and_repeated_captions_fail(self):
        document = self.document([[(100, 'h', 9), (140, 'Slika 1.1: Tank', 9.5),
                                   (180, 'h', 9), (220, 'Slika 1.1: Tank', 9.5)]])
        issues = figure_label_issues(document, {'1.1': ['h'], '1.2': ['v']})
        self.assertTrue(any('ponovljena' in issue for issue in issues))
        self.assertTrue(any('slika 1.2' in issue for issue in issues))

    def test_unicode_and_wrapping_preserve_the_actual_symbol(self):
        self.assertEqual(_normalise_label('A\u00a0=\n2 m²'), 'A=2m2')
        self.assertNotEqual(_normalise_label('n̂'), _normalise_label('n'))

    def test_only_figure_objects_need_numbered_captions(self):
        objects = {'fig-first': {'kind': 'Figure', 'number': '11.1'},
                   'fig-legacy-prose': {'kind': 'Section', 'number': '11.2'},
                   'fig-last': {'kind': 'Figure', 'number': '11.2'}}
        captions = ['Slika\u00a011.1: First\nSlika 11.2: Last']
        self.assertEqual(_figure_numbering_issues(captions, objects), [])
        self.assertTrue(_figure_numbering_issues(['Slika 11.1: First'], objects))
        self.assertTrue(_figure_numbering_issues(['Slika 11.2: Last\nSlika 11.1: First'], objects))
        self.assertTrue(_figure_numbering_issues(captions + ['Slika 12.1: Extra'], objects))


if __name__ == '__main__':
    unittest.main()
