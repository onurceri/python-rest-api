from django.test import TestCase
from datetime import date

from core.models import customer_model


class CustomerTests(TestCase):
    def test_customer_name(self):
        customer = customer_model.Customer.objects.create(
            id=1,
            name='test_customer',
            created_at=date.today(),
            is_active=True,
            is_deleted=False
        )

        self.assertEqual(str(customer), customer.name)
