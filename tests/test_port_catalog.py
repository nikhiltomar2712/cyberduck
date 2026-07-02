import unittest

from cyberduck.port_catalog import describe_port, is_risky_public_port, summarize_ports


class PortCatalogTests(unittest.TestCase):
    def test_ports(self):
        self.assertEqual(describe_port(22), "SSH")
        self.assertTrue(is_risky_public_port(3389))
        self.assertIn("443: HTTPS", summarize_ports([443]))


if __name__ == "__main__":
    unittest.main()
