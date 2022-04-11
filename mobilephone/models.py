from django.db import models

# Create your models here.
class MobilePhoneA(models.Model):
    name = models.CharField(max_length=50, default='')
    image = models.TextField(max_length=255, default='https://cdn-amz.fadoglobal.io/images/I/71hIfcIPyxS.jpg')
    storage = models.IntegerField(default=0)
    screensize = models.CharField(max_length=50, default='')
    ram = models.CharField(max_length=50, default='')
    chip = models.CharField(max_length=50, default='')
    os = models.CharField(max_length=50, default='')
    description = models.TextField(max_length=255, default='')

    def __str__(self):
        return self.name


class MobilePhoneItem(models.Model):
    mobilePhone = models.ForeignKey(MobilePhoneA, on_delete=models.CASCADE)
    price = models.FloatField(max_length=50)
    discount = models.CharField(max_length=50)
    inventory = models.IntegerField(default=0)