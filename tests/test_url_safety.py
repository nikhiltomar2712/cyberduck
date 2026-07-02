import unittest

from cyberduck.url_safety import is_https_url, normalize_url, suspicious_url_reasons


class UrlSafetyTests(unittest.TestCase):
    def test_url_reasons(self):
        self.assertEqual(normalize_url("example.com"), "https://example.com")
        self.assertTrue(is_https_url("example.com"))
        self.assertIn("ip_address_host", suspicious_url_reasons("http://192.0.2.1/login"))


if __name__ == "__main__":
    unittest.main()
