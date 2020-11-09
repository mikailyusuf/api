from django.db import models

# Create your models here.


class Customers(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
