from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Account(models.Model):
    username = models.CharField(default='', max_length=50, unique=True)
    password = models.CharField(default='', max_length=50)

    def __str__(self):
        return self.username


class Address(models.Model):
    city = models.CharField(default='HaNoi', max_length=50)
    district = models.CharField(default='HaNoi', max_length=50)
    street = models.CharField(default='HaNoi', max_length=50)
    number = models.IntegerField(default=1)

    def __str__(self):
        return self.city


class Fullname(models.Model):
    firstname = models.CharField(default='', max_length=50)
    lastname = models.CharField(default='', max_length=50)

    def __str__(self):
        return self.lastname


class Customer(models.Model):
    number = models.IntegerField(default=0)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50, default='')
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    fullname = models.ForeignKey(Fullname, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.email



