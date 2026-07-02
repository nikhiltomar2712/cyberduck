import unittest

from cyberduck.models import RiskItem
from cyberduck.risk_matrix import risk_label, risk_score, sort_risks


class RiskMatrixTests(unittest.TestCase):
    def test_risk_scoring(self):
        self.assertEqual(risk_score(5, 5), 25)
        self.assertEqual(risk_label(25), "critical")
        sorted_items = sort_risks([RiskItem("low", 1, 1), RiskItem("high", 5, 5)])
        self.assertEqual(sorted_items[0].name, "high")


if __name__ == "__main__":
    unittest.main()
