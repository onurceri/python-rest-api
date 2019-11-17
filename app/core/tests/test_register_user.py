import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse


# initialize the APIClient app
client = Client()


class UserRegisterTest(TestCase):
    """ Test module for user register """

    def setUp(self):
        self.valid_identity = {
            "email": "helloworld@mailaddress.com",
            "username": "helloworld",
            "password": "password123"
        }
        self.invalid_identity = {
            "email": "helloworld@mailaddress.com",
            "username": "helloworld"
        }

    def test_user_valid_identity(self):
        response = client.post(
            reverse('user-register-api'),
            content_type='application/json',
            data=json.dumps(self.valid_identity),
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_invalid_identity(self):
        response = client.post(
            reverse('user-register-api'),
            content_type='application/json',
            data=json.dumps(self.invalid_identity),
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
