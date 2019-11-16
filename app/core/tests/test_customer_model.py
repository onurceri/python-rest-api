from django.test import TestCase
from core.models.customer_model import Customer


class CustomerTest(TestCase):
    """ Test module for Customer model """

    def setUp(self):
        Customer.objects.create(
            first_name='John', last_name='Clay', age=34, mail_address='john@email.com')
        Customer.objects.create(
            first_name='Dennis', last_name='Libre', age=34, mail_address='dennis@email.com')

    def test_customer_fullname(self):
        customer_john = Customer.objects.get(first_name='John')
        customer_dennis = Customer.objects.get(first_name='Dennis')
        self.assertEqual(
            customer_john.get_fullname(), "John Clay")
        self.assertEqual(
            customer_dennis.get_fullname(), "Dennis Libre")
