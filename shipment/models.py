from django.db import models
from django.utils.translation import gettext_lazy as _
<<<<<<< HEAD


# Create your models here.
=======
# from cart.models import Order

# Create your models here.


>>>>>>> 30db7932ae71e0e5a3c490ef335e531737262139
class ShipmenCost(models.Model):
    name = models.CharField(default='', max_length=50)
    price = models.FloatField(max_length=50, default=0)


class Shipment(models.Model):
    SELECTION = (
        (1, _('Low')),
        (2, _('Fast')),
        (3, _('Take away')),
    )
    # [...]
    selection = models.PositiveSmallIntegerField(
        choices=SELECTION,
        default=2,
    )
    address = models.CharField(default='', max_length=50)
    codShip = models.TextField(default='', max_length=50)

    def __str__(self):
        return self.codShip
