from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class CategoryBook(models.Model):
    name = models.CharField(default='', max_length=50)
    description = models.TextField(default='')

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(default='', max_length=50)
    address = models.TextField(default='')

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(default='', max_length=50)
    biography = models.TextField(default='')

    def __str__(self):
        return self.name


class BookEn(models.Model):
    ISBN = models.CharField(primary_key=True, max_length=50)
    title = models.TextField(default='')
    summary = models.CharField(max_length=255, default='')
    numberOfPages = models.IntegerField(default=0)
    language = models.CharField(max_length=50, default='')
    image = models.TextField(max_length=255, default='https://cdn5.f-cdn.com/contestentries/1840252/39964678/5fa3d8364496e_thumb900.jpg')
    categoryBook = models.ForeignKey(CategoryBook, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class BookItem(models.Model):
    book = models.ForeignKey(BookEn, on_delete=models.CASCADE)
    barcode = models.CharField(primary_key=True, max_length=50)
    price = models.FloatField(max_length=50)
    discount = models.CharField(max_length=50)
    inventory = models.IntegerField(default=0)



