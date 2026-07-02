import unittest

from cyberduck.crypto_policy import crypto_recommendation, is_tls_version_acceptable, weak_hash_algorithm


class CryptoPolicyTests(unittest.TestCase):
    def test_crypto_policy(self):
        self.assertTrue(weak_hash_algorithm("sha1"))
        self.assertTrue(is_tls_version_acceptable("TLS 1.3"))
        self.assertIn("SHA-256", crypto_recommendation("md5"))


if __name__ == "__main__":
    unittest.main()
