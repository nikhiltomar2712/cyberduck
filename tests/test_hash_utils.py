import unittest

from cyberduck.hash_utils import hash_text, hashes_match


class HashUtilsTests(unittest.TestCase):
    def test_hash_text_and_compare(self):
        digest = hash_text("cyberduck")
        self.assertTrue(hashes_match(digest, digest.upper()))
        self.assertFalse(hashes_match(digest, hash_text("other")))


if __name__ == "__main__":
    unittest.main()
