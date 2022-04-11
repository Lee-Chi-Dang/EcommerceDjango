from django import forms
from .models import TypeClothes, BrandClothes, ClothesA, ClothesItem

class TypeClothesForm(forms.ModelForm):
    class Meta:
        model = TypeClothes
        fields = '__all__'

class BrandClothesForm(forms.ModelForm):
    class Meta:
        model = BrandClothes
        fields = '__all__'


class ClothesForm(forms.ModelForm):
    class Meta:
        model = ClothesA
        fields = '__all__'


class ClothesItemForm(forms.ModelForm):
    class Meta:
        model = ClothesItem
        fields = '__all__'