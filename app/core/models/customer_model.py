from django.db import models
from django.conf import settings

class Customer(models.Model):
    """Customer model"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created_at = models.DateField()
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)


    def __str__(self):
        return self.name
