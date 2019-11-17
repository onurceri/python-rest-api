import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


# initialize the APIClient app
client = Client()


class UserLoginTest(TestCase):
    """ Test module for user login """

    def setUp(self):
        User.objects.create_user(
            username='test_user',
            email='test_user@mail.com',
            password='password123'
        )
        self.valid_identity = {
            'username': 'test_user',
            'password': 'password123'
        }
        self.invalid_identity = {
            'username': 'test_user',
            'password': 'password12345'
        }

    def test_user_valid_identity(self):
        response = client.post(
            reverse('user-login-api'),
            content_type='application/json',
            data=json.dumps(self.valid_identity),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_invalid_identity(self):
        response = client.post(
            reverse('user-login-api'),
            content_type='application/json',
            data=json.dumps(self.invalid_identity),
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
