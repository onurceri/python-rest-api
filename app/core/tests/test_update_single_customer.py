import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse

from core.models.customer_model import Customer


# initialize the APIClient app
client = Client()


class UpdateSingleCustomerTest(TestCase):
    """ Test module for updating an existing customer record """

    def setUp(self):
        self.john = Customer.objects.create(
            first_name='John', last_name='Clay', age=34, mail_address='john@email.com')
        self.dennis = Customer.objects.create(
            first_name='Dennis', last_name='Libre', age=42, mail_address='dennis@email.com')
        self.valid_payload = {
            'first_name': 'John',
            'last_name': 'Clay',
            'age': 48,
            'mail_address': 'clay@email.com'
        }
        self.invalid_payload = {
            'first_name': '',
            'last_name': 'Jefferson',
            'age': 12,
            'mail_address': 'jeff@email.com'
        }

    def test_valid_update_customer(self):
        response = client.put(
            reverse('queryable-customer-api', kwargs={'pk': self.john.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_customer(self):
        response = client.put(
            reverse('queryable-customer-api', kwargs={'pk': self.john.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
