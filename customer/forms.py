from django import forms
from .models import Account, Address, Fullname, Customer


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'
