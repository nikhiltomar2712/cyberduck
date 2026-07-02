import unittest

from cyberduck.password_policy import estimate_entropy_bits, evaluate_password


class PasswordPolicyTests(unittest.TestCase):
    def test_strong_password_scores_higher(self):
        weak = evaluate_password("password")
        strong = evaluate_password("CorrectHorseBatteryStaple!42")
        self.assertGreater(strong.score, weak.score)
        self.assertGreater(estimate_entropy_bits("Abc123!@#"), 0)


if __name__ == "__main__":
    unittest.main()
