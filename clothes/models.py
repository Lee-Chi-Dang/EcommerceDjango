from django.db import models

# Create your models here.
class TypeClothes(models.Model):
    name = models.CharField(default='', max_length=50)
    description = models.TextField(default='')
    sex = models.CharField(default='', max_length=50)

    def __str__(self):
        return self.name

class BrandClothes(models.Model):
    name = models.CharField(default='', max_length=50)
    address = models.TextField(default='')

    def __str__(self):
        return self.name


class ClothesA(models.Model):
    name = models.CharField(max_length=50, default='')
    collection = models.CharField(max_length=50, default='')
    material = models.CharField(max_length=50, default='')
    size = models.CharField(max_length=50, default='')
    color = models.CharField(max_length=50, default='')
    image = models.TextField(max_length=255, default='https://assets.vogue.com/photos/62274b72c0d4fbe60f143e7e/master/w_2560%2Cc_limit/00001-chanel-fall-2022-ready-to-wear-paris-credit-gorunway.jpg')
    typeClothes = models.ForeignKey(TypeClothes, on_delete=models.CASCADE)
    brandClothes = models.ForeignKey(BrandClothes, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ClothesItem(models.Model):
    clothes = models.ForeignKey(ClothesA, on_delete=models.CASCADE)
    price = models.FloatField(max_length=50)
    discount = models.CharField(max_length=50)
    inventory = models.IntegerField(default=0)
