from django import forms
from .models import MobilePhoneA, MobilePhoneItem

class MobilePhoneForm(forms.ModelForm):
    class Meta:
        model = MobilePhoneA
        fields = '__all__'


class MobilePhoneItemForm(forms.ModelForm):
    class Meta:
        model = MobilePhoneItem
        fields = '__all__'

