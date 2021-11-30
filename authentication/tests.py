from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from authentication import models as authentication
from rest_framework import status


class AccountsTest(APITestCase):
    def setUp(self):
        # We want to go ahead and originally create a user.
        self.test_user = authentication.User.objects.create_user(
            name="admin",
            email="admin@gmail.com",
            password="admin",
        )

        # URL for creating an account.
        self.signin_url = reverse("authentication:signin")
        self.signup_url = reverse("authentication:signup")

    def test_create_user(self):
        """
        Ensure we can create a new user and a valid token is created with it.
        """
        data = {
            "name": "endalk",
            "email": "endalk@endalk.com",
            "password": "endalk",
        }

        response = self.client.post(self.signup_url, data, format="json")

        # We want to make sure we have two users in the database..
        self.assertEqual(authentication.User.objects.count(), 2)
        # And that we're returning a 201 created code.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Additionally, we want to return the username and email upon successful creation.
        self.assertEqual(response.data["name"], data["name"])
        self.assertEqual(response.data["email"], data["email"])
        self.assertFalse("password" in response.data)

    def test_login(self):
        """
        Ensure we can create a new user and a valid token is created with it.
        """
        data = {
            "email": "admin@gmail.com",
            "password": "admin",
        }

        response = self.client.post(self.signin_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], data["email"])
        self.assertFalse("password" in response.data)
