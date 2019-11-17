import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# initialize the APIClient app
client = Client()


class CreateNewCustomerTest(TestCase):
    """ Test module for inserting a new customer """

    def setUp(self):
        self.valid_payload = {
            'first_name': 'John',
            'last_name': 'Clay',
            'age': '34',
            'mail_address': 'john@email.com'
        }
        self.invalid_payload = {
            'first_name': '',
            'last_name': 'Clay',
            'age': '34',
            'mail_address': 'john@email.com'
        }
        dummy_user = User.objects.create(
            username='test_user',
            email='test_user@mail.com',
            password='password123'
        )
        token, _ = Token.objects.get_or_create(user=dummy_user)
        self.header = {'HTTP_AUTHORIZATION': 'Token ' + token.key}

    def test_create_valid_customer(self):
        response = client.post(
            reverse('customer-api'),
            content_type='application/json',
            data=json.dumps(self.valid_payload),
            **self.header
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_customer(self):
        response = client.post(
            reverse('customer-api'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json',
            **self.header
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
