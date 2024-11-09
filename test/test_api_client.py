import unittest
from src.api_client import get_location
from unittest.mock import patch

class ApiClientTest(unittest.TestCase):

    @patch()
    def test_get_location_returns_expected_data(self):
        result = get_location("8.8.8.8")
        self.assertEqual(
            result.get("country"),
            "United States of America"
        )