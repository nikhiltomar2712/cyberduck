import unittest

from cyberduck.secret_patterns import find_potential_secrets


class SecretPatternTests(unittest.TestCase):
    def test_secret_detection(self):
        self.assertIn("generic_secret", find_potential_secrets("api_key = 'abcdefghijk'"))
        self.assertEqual(find_potential_secrets("normal text"), [])


if __name__ == "__main__":
    unittest.main()
