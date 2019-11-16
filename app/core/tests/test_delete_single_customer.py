from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse

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

    def test_valid_delete_customer(self):
        response = client.delete(
            reverse('get_delete_update_customer', kwargs={'pk': self.john.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_customer(self):
        response = client.delete(
            reverse('get_delete_update_customer', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
