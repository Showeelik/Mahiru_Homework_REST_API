from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

from subscriptions.models import Subscription
from .models import Course, Lesson


User = get_user_model()

class CourseTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="testuser@example.com", username="test", password="password123")
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(name="Test Course", description="Description", owner=self.user)

    def test_create_course(self):
        data = {"name": "New Course", "description": "New Description"}
        response = self.client.post("/api/courses/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_subscribe_to_course(self):
        data = {"course_id": self.course.id}
        response = self.client.post("/api/subscriptions/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Подписка добавлена")
        self.assertTrue(Subscription.objects.filter(user=self.user, course=self.course).exists())

    def test_unsubscribe_from_course(self):
        Subscription.objects.create(user=self.user, course=self.course)
        data = {"course_id": self.course.id}
        response = self.client.post("/api/subscriptions/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Подписка удалена")
        self.assertFalse(Subscription.objects.filter(user=self.user, course=self.course).exists())
