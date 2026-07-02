import unittest

from cyberduck.header_policy import grade_headers, missing_headers


class HeaderPolicyTests(unittest.TestCase):
    def test_missing_and_grade(self):
        headers = {"Content-Security-Policy": "default-src 'self'"}
        self.assertIn("strict-transport-security", missing_headers(headers))
        self.assertEqual(grade_headers({"Content-Security-Policy": "x", "Strict-Transport-Security": "x", "X-Content-Type-Options": "nosniff", "Referrer-Policy": "no-referrer", "Permissions-Policy": "geolocation=()"}), "A")


if __name__ == "__main__":
    unittest.main()
