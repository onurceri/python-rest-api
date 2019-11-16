from django.db import models
from core.models import customer_model


class CustomerMailAddress(models.Model):
    """Customer mail address model"""
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(
        customer_model.Customer, related_name='mail_addresses', on_delete=models.CASCADE)
    mail_address = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.mail_address
