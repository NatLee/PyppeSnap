import unittest
import pytest
from pathlib import Path

from pyppesnap import get_snapshot_by_url

class TestPyppeSnap(unittest.TestCase):

    def test_get_snapshot_by_url(self):
        url = 'https://www.google.com'
        base64_data = get_snapshot_by_url(url)
        base64_data
        self.assertIsNotNone(base64_data)

if __name__ == '__main__':
    unittest.main()
