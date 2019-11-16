from django.db import models


class CustomerType(models.Model):
    """Customer type model"""
    id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.type_name
