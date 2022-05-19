from django.db import models
from shipment.models import Shipment

# Create your models here.
class Order(models.Model):
    status = models.TextField(max_length=50, default='')
    amount = models.IntegerField(null=False)
    date = models.DateTimeField(auto_now=True, blank=True)
    def __int__(self):
        return self.id


class Cart(models.Model):
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE)
    order_no = models.TextField(max_length=255, default='Order')
    proId = models.IntegerField(null=False)
    proPrice = models.IntegerField(null=False)
    proImage = models.TextField(max_length=255, default='https://cdn5.f-cdn.com/contestentries/1840252/39964678/5fa3d8364496e_thumb900.jpg')
    proQuantity = models.IntegerField(null=False)

