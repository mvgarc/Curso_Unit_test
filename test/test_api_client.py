import unittest
from src.api_client import get_location

class ApiClientTest(unittest.TestCase):

    def test_get_location_returns_expected_data(self):
        result = get_location("8.8.8.8")