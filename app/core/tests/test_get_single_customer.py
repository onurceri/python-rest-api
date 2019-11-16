from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse

from core.models.customer_model import Customer
from core.serializers import CustomerSerializer


# initialize the APIClient app
client = Client()


class GetSingleCustomerTest(TestCase):
    """ Test module for GET single customer API """

    def setUp(self):
        self.john = Customer.objects.create(
            first_name='John', last_name='Clay', age=34, mail_address='john@email.com')
        self.dennis = Customer.objects.create(
            first_name='Ronald', last_name='Libre', age=42, mail_address='ronald@email.com')
        self.donald = Customer.objects.create(
            first_name='Donald', last_name='Hoff', age=56, mail_address='donald@email.com')
        self.sam = Customer.objects.create(
            first_name='Sam', last_name='Brain', age=19, mail_address='sam@email.com')

    def test_get_valid_single_customer(self):
        response = client.get(
            reverse('get_delete_update_customer', kwargs={'pk': self.sam.pk}))
        customer = Customer.objects.get(pk=self.sam.pk)
        serializer = CustomerSerializer(customer)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_customer(self):
        response = client.get(
            reverse('get_delete_update_customer', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
