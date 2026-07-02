import unittest

from cyberduck.mfa_policy import best_mfa_method, mfa_strength, recommend_upgrade


class MfaPolicyTests(unittest.TestCase):
    def test_mfa_methods(self):
        self.assertGreater(mfa_strength("hardware_key"), mfa_strength("sms"))
        self.assertEqual(best_mfa_method(["sms", "totp"]), "totp")
        self.assertIn("authenticator", recommend_upgrade("sms"))


if __name__ == "__main__":
    unittest.main()
