import unittest

from cyberduck.cidr_utils import contains_ip, network_summary


class CidrUtilsTests(unittest.TestCase):
    def test_network_helpers(self):
        self.assertTrue(contains_ip("192.168.1.0/24", "192.168.1.5"))
        self.assertEqual(network_summary("10.0.0.1/24")["prefixlen"], 24)


if __name__ == "__main__":
    unittest.main()
