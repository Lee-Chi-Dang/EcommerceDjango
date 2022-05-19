from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

from book.models import BookItem
# Create your views here.

def index(request):
    return render(request, 'home/index.html')
def adminpage(request):
    return render(request, 'home/admin.html')
