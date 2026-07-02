import unittest
from datetime import datetime

from cyberduck.incident_timeline import TimelineEvent, render_timeline, sort_events


class IncidentTimelineTests(unittest.TestCase):
    def test_timeline_sorting(self):
        later = TimelineEvent(datetime(2026, 1, 2), "later")
        earlier = TimelineEvent(datetime(2026, 1, 1), "earlier")
        self.assertEqual(sort_events([later, earlier])[0].title, "earlier")
        self.assertIn("earlier", render_timeline([later, earlier]))


if __name__ == "__main__":
    unittest.main()
