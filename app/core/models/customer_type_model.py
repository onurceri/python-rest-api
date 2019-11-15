from django.db import models
from django.conf import settings

class CustomerType(models.Model):
    """Customer type model"""
    id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)