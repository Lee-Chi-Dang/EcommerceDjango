from django import forms
from django.db import models
from .models import ContactABC

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactABC
        fields = '__all__'
    widgets = {
        'comment': forms.Textarea(attrs={'cols': 100, 'rows': 40})
    }
    labels = {
        'name': 'fullname',
        'comment': 'Issues'
    }
    help_texts = {
        'comment': 'Write your problem'
    }




