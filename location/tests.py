from django.test import TestCase, Client
from unittest.mock import patch

# Create your tests here.
class LocationSearchViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    @patch("location.services.LocationService.search_location")
    def test_department_search_basic(self, mock_search):
        mock_departments = [
            type("Location", (), {
                "id": "11111111-1111-1111-1111-111111111115",
                "name": "Somewhere",
                "address": "in",
                "city": "Miami",
                "organization_id": "11111111-1111-1111-1111-111111111111"
            })(),
        ]
        mock_search.return_value = mock_departments

        response = self.client.get("/location/search/", {"keyword": "Miami", "page": 1, "page_size": 2})
        self.assertEqual(response.status_code, 200)

        json_data = response.json()
        self.assertIn("total", json_data)
        self.assertIn("page", json_data)
        self.assertIn("page_size", json_data)
        self.assertIn("results", json_data)

        # Pagination works: only 2 results per page
        self.assertEqual(json_data["page_size"], 2)
        self.assertEqual(json_data["page"], 1)
        self.assertEqual(len(json_data["results"]), 1)

    @patch("location.services.LocationService.search_location")
    def test_location_search_empty(self, mock_search):
        """Test when no locations match the keyword"""
        mock_search.return_value = []
        response = self.client.get("/location/search/", {"keyword": "test", "page": 1, "page_size": 5})
        self.assertEqual(response.status_code, 200)
        json_data = response.json()
        self.assertEqual(json_data["total"], 0)
        self.assertEqual(len(json_data["results"]), 0)
