from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=255, null=False,unique=True)
    email = models.EmailField(max_length=255, null=False,unique=True)
    password = models.CharField(max_length=50)
    ifLogged = models.BooleanField(default=False)
    token = models.CharField(max_length=500, null=True, default="")

    def __str__(self):
        return "{} -{}".format(self.username, self.email)


class Customers(models.Model):
    # user = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    profile_pic = models.ImageField(null=True, blank=True)
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
