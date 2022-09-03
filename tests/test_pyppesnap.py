import unittest
import pytest
from pathlib import Path

from pyppesnap import get_image_snapshot_by_url, get_pdf_snapshot_by_url

class TestPyppeSnap(unittest.TestCase):

    test_url = 'https://www.google.com'

    def test_get_image_snapshot_by_url(self):
        
        base64_data = get_image_snapshot_by_url(self.test_url)
        base64_data
        self.assertIsNotNone(base64_data)

    def test_get_pdf_snapshot_by_url(self):
        url = 'https://www.google.com'
        base64_data = get_pdf_snapshot_by_url(self.test_url)
        base64_data
        self.assertIsNotNone(base64_data)

if __name__ == '__main__':
    unittest.main()
