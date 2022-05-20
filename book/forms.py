from django import forms
from .models import Author, CategoryBook, Publisher, BookEn, BookItem


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'


class CategoryBookForm(forms.ModelForm):
    class Meta:
        model = CategoryBook
        fields = '__all__'


class BookForm(forms.ModelForm):
    class Meta:
        model = BookEn
        fields = '__all__'


class BookItemForm(forms.ModelForm):
    class Meta:
        model = BookItem
        fields = '__all__'