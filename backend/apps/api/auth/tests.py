from http.cookies import SimpleCookie

from apps.api.auth.models import User
from apps.api.questioning.models import Questionnaire
from apps.api.reference.models import Department, Faculty, Position, Rate
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class AuthTests(APITestCase):
    """
    Тестирование приложения аутентификации
    """

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            "admin", "admin@admin.com", "admin"
        )
        self.token = ""
        faculty = Faculty.objects.create(short_name="test", name="test")
        self.department = Department.objects.create(
            faculty=faculty, short_name="test", name="test"
        )
        self.rate = Rate.objects.create(value=33.2)
        self.position = Position.objects.create(name="test")
        self.questionnaire = Questionnaire.objects.create(
            name="name", status=1
        )

    def login(self):
        """
        Авторизация администратора
        """
        url = "/api/v1/auth/token/login/"
        data = {
            "username": "admin",
            "password": "admin",
        }
        response = self.client.post(url, data, format="json")
        self.token = response.data["access_token"]

    def test_create_user_positions(self):
        """
        Тестирование создания должности пользователя
        """
        self.login()

        url = "/api/v1/auth/create-user/"

        data = {
            "username": "username",
            "password": "kyhbkiYGKUYHGGHkk",
            "first_name": "first_name",
            "last_name": "last_name",
            "patronymic": "patronymic",
            "user_image": None,
            "user_positions": [
                {
                    "department": self.department.id,
                    "rate": self.rate.id,
                    "position": self.position.id,
                }
            ],
            "questionnaire": [self.questionnaire.id],
        }

        self.client.cookies = SimpleCookie({"access_token": self.token})

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # self.assertEqual(Account.objects.count(), 1)
        # self.assertEqual(Account.objects.get().name, "DabApps")
