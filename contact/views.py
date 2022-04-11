from django.shortcuts import render
from django.views import View
from .forms import ContactForm
from .models import ContactABC
from django.http import HttpResponse

# Create your views here.
class Contact(View):
    def get(self, request):
        cf = ContactForm
        contacts = ContactABC.objects.all()
        return render(request, 'contact/contact.html', {'cf': cf, 'contacts': contacts})
    def post(self, request):
        if request.method == 'POST':
            contact = ContactForm(request.POST)
            if contact.is_valid():
                contact.save()
                return HttpResponse('Thanh cong')