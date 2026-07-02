import unittest

from cyberduck.models import Finding
from cyberduck.report_builder import finding_to_markdown, markdown_report


class ReportBuilderTests(unittest.TestCase):
    def test_report_markdown(self):
        finding = Finding("Missing MFA", "high", "Admin account", "Enable MFA")
        self.assertIn("Missing MFA", finding_to_markdown(finding))
        self.assertTrue(markdown_report("Review", [finding]).startswith("# Review"))


if __name__ == "__main__":
    unittest.main()
