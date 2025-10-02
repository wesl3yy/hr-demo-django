from django.test import TestCase, Client
from unittest.mock import patch

# Create your tests here.
class UserSearchViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    @patch("user.services.UserService.search")
    def test_department_search_basic(self, mock_search):
        mock_departments = [
            type("UserProfile", (), 
            {
                "id": "11111111-1111-1111-1111-111111111119",
                "first_name": "John",
                "last_name": "Doe",
                "email": "john@example.com",
                "phone": "1234",
                "status": "t",
                "organization_id": "11111111-1111-1111-1111-111111111111",
                "department_id": "11111111-1111-1111-1111-111111111111",
                "location_id": "11111111-1111-1111-1111-111111111115",
                "position_id": "11111111-1111-1111-1111-111111111117",
                "manager_id": None
            })(),
            type("UserProfile", (),
            {
                "id": "11111111-1111-1111-1111-111111111120",
                "first_name": "Alicia",
                "last_name": "Doe",
                "email": "alicia@example.com",
                "phone": "1234",
                "status": "t",
                "organization_id": "11111111-1111-1111-1111-111111111111",
                "department_id": "11111111-1111-1111-1111-111111111111",
                "location_id": "11111111-1111-1111-1111-111111111115",
                "position_id": "11111111-1111-1111-1111-111111111117",
                "manager_id": None
            })()
        ]
        mock_search.return_value = mock_departments

        response = self.client.get("/employee/search/", {"keyword": "Doe", "page": 1, "page_size": 2})
        self.assertEqual(response.status_code, 200)

        json_data = response.json()
        self.assertIn("total", json_data)
        self.assertIn("page", json_data)
        self.assertIn("page_size", json_data)
        self.assertIn("results", json_data)

        # Pagination works: only 2 results per page
        self.assertEqual(json_data["page_size"], 2)
        self.assertEqual(json_data["page"], 1)
        self.assertEqual(len(json_data["results"]), 2)

    @patch("user.services.UserService.search")
    def test_user_search_empty(self, mock_search):
        """Test when no users match the keyword"""
        mock_search.return_value = []
        response = self.client.get("/employee/search/", {"keyword": "test", "page": 1, "page_size": 5})
        self.assertEqual(response.status_code, 200)
        json_data = response.json()
        self.assertEqual(json_data["total"], 0)
        self.assertEqual(len(json_data["results"]), 0)
