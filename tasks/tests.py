# tasks/tests.py

from rest_framework.test import APITestCase


class HealthCheckTests(APITestCase):
    def test_health_endpoint_returns_200(self):
        """
        Ensure the /health/ endpoint returns a 200 OK status.
        """
        # Simulate a GET request to /health/
        response = self.client.get('/health/')

        # Assert the HTTP status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert the JSON response contains the expected key-value pair
        self.assertEqual(response.data, {"status": "healthy"})
