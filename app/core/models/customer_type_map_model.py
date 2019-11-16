from django.db import models

from core.models import customer_model
from core.models import customer_type_model


class CustomerTypeMap(models.Model):
    """Customer type map model"""
    id = models.AutoField(primary_key=True)
    customertype = models.ForeignKey(
        customer_type_model.CustomerType, related_name='type', on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(
        customer_model.Customer, related_name='customer', on_delete=models.CASCADE, null=True)
