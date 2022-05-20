from django import forms
from .models import Cart, Order, Payment


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = '__all__'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['type']