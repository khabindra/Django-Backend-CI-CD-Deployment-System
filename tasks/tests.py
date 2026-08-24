# tasks/tests.py

from rest_framework.test import APITestCase
from .models import Task


class HealthCheckTests(APITestCase):
    def test_health_endpoint_returns_200(self):
        response = self.client.get('/health/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"status": "healthy"})

class TaskModelTests(APITestCase):
    def test_create_task(self):
        task = Task.objects.create(title="Learn CI/CD")
        self.assertEqual(task.title, "Learn CI/CD")
        self.assertFalse(task.completed)
        self.assertEqual(str(task), "Learn CI/CD")


