from django.contrib import admin
from .models import CategoryBook, Author,Publisher, BookEn, BookItem

# Register your models here.
admin.site.register(CategoryBook)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(BookEn)
admin.site.register(BookItem)