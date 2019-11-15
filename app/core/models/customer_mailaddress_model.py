from django.db import models
from django.conf import settings
from core.models import customer_model

class CustomerMailAddress(models.Model):
    """Customer mail address model"""
    id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(customer_model.Customer, on_delete=models.CASCADE)
    mail_address = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)