from django.db import models
from django.utils.translation import gettext_lazy as _
from shipment.models import Shipment


# Create your models here.
class Payment(models.Model):
    amount = models.FloatField(null=False)
    TYPE = (
        (1, _('Paypal')),
        (2, _('Cast')),
    )
    # [...]
    type = models.PositiveSmallIntegerField(
        choices=TYPE,
        default=2,
    )


class Order(models.Model):
    status = models.TextField(max_length=50, default='')
    amount = models.IntegerField(null=False)
    date = models.DateTimeField(auto_now=True, blank=True)
    shipment = models.ForeignKey(Shipment, default=None, on_delete=models.CASCADE)
    customerId = models.IntegerField(null=False, default=1)
    paymentId = models.IntegerField(null=False, default=2)


class Cart(models.Model):
    proId = models.IntegerField(null=False)
    proPrice = models.IntegerField(null=False)
    proImage = models.TextField(max_length=255, default='https://cdn5.f-cdn.com/contestentries/1840252/39964678/5fa3d8364496e_thumb900.jpg')
    proQuantity = models.IntegerField(null=False)
    order = models.ForeignKey(Order, default=None, on_delete=models.CASCADE)


