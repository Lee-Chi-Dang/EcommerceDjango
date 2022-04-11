from django.db import models

# Create your models here.
class ContactABC(models.Model):
    name = models.CharField(default='', max_length=50)
    email = models.EmailField()
    comment = models.TextField(default='', max_length=5)