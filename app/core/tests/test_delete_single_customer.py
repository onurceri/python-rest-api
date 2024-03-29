from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from core.models.customer_model import Customer


# initialize the APIClient app
client = Client()


class DeleteSingleCustomerTest(TestCase):
    """ Test module for deleting an existing customer record """

    def setUp(self):
        self.john = Customer.objects.create(
            first_name='John', last_name='Clay', age=34, mail_address='john@email.com')
        self.dennis = Customer.objects.create(
            first_name='Dennis', last_name='Libre', age=42, mail_address='dennis@email.com')
        dummy_user = User.objects.create(
            username='test_user', email='test_user@mail.com', password='password123')
        token, _ = Token.objects.get_or_create(user=dummy_user)
        self.header = {'HTTP_AUTHORIZATION': 'Token ' + token.key}

    def test_valid_delete_customer(self):
        response = client.delete(
            reverse('queryable-customer-api', kwargs={'pk': self.john.pk}), **self.header)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_customer(self):
        response = client.delete(
            reverse('queryable-customer-api', kwargs={'pk': 30}), **self.header)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
