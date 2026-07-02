import unittest

from cyberduck.dns_utils import normalize_record_name, parse_hosts_lines


class DnsUtilsTests(unittest.TestCase):
    def test_hosts_parsing(self):
        self.assertEqual(normalize_record_name("Example.COM."), "example.com")
        records = parse_hosts_lines(["127.0.0.1 localhost local.test # comment"])
        self.assertEqual(records["local.test"], "127.0.0.1")


if __name__ == "__main__":
    unittest.main()
