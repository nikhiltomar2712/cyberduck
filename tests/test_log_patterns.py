import unittest

from cyberduck.log_patterns import count_failed_login_ips, extract_ips, failed_login_lines


class LogPatternTests(unittest.TestCase):
    def test_failed_login_counter(self):
        lines = ["Failed password from 192.0.2.1", "Accepted password from 192.0.2.2", "Invalid user from 192.0.2.1"]
        self.assertEqual(extract_ips(lines[0]), ["192.0.2.1"])
        self.assertEqual(len(failed_login_lines(lines)), 2)
        self.assertEqual(count_failed_login_ips(lines)["192.0.2.1"], 2)


if __name__ == "__main__":
    unittest.main()
