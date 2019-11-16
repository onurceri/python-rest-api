from django.db import models


class Customer(models.Model):
    """
    Customer Model
    Defines the attributes of a customer
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    mail_address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_fullname(self):
        return self.first_name + ' ' + self.last_name

    def __repr__(self):
        return self.first_name + ' ' + self.last_name + ' is added.'
