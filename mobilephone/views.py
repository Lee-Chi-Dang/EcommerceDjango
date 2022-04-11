from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.shortcuts import redirect

from .models import MobilePhoneA, MobilePhoneItem
from .forms import MobilePhoneForm, MobilePhoneItemForm

# Create your views here.
class MobilePhoneABC(View):
    def get(self, request):
        mobilephoneItemList = MobilePhoneItem.objects.all()
        return render(request, 'mobilephone/mobilePhone.html', {
            'mobilephoneItemList': mobilephoneItemList,
        })


class MobilephoneController(View):
    def get(self, request):
        mobilephoneAList = MobilePhoneA.objects.all()
        mobilephoneItemList = MobilePhoneItem.objects.all()
        return render(request, 'mobilephone/mobilephoneController.html', {
            'mobilephoneAList': mobilephoneAList,
            'mobilephoneItemList': mobilephoneItemList,
        })


#----------------------- mobilePhone ------------------------------
class MobilePhoneFormView(View):
    def get(self, request):
        af = MobilePhoneForm()
        return render(request, 'mobilephone/mobilephoneForm.html', {'af': af})
    def post(self, request):
        if request.method == 'POST':
            mobilePhoneForm = MobilePhoneForm(request.POST)
            if mobilePhoneForm.is_valid():
                mobilePhoneForm.save()
                return redirect('/mobilephone/mobilephoneController/')


class MobilePhoneFormUpdateView(View):
    def get(self, request, id):
        mobilePhone = MobilePhoneA.objects.get(id=id)
        af = MobilePhoneForm(instance=mobilePhone)
        return render(request, 'mobilephone/mobilephoneForm.html', {'af': af})
    def post(self, request, id):
        if request.method == 'POST':
            mobilePhone = MobilePhoneA.objects.get(id=id)
            mobilePhoneForm = MobilePhoneForm(request.POST, instance=mobilePhone)
            if mobilePhoneForm.is_valid():
                mobilePhoneForm.save()
                return redirect('/mobilephone/mobilephoneController/')


class MobilePhoneFormDeleteView(View):
    def get(self, request, id):
        mobilePhone = MobilePhoneA.objects.get(id=id)
        af = MobilePhoneForm(instance=mobilePhone)
        return render(request, 'mobilephone/delete.html', {'af': af, 'item': mobilePhone})
    def post(self, request, id):
        if request.method == 'POST':
            mobilePhone = MobilePhoneA.objects.get(id=id)
            mobilePhone.delete()
            return redirect('/mobilephone/mobilephoneController/')


#----------------------- MobilePhoneItem ------------------------------
class MobilePhoneItemFormView(View):
    def get(self, request):
        af = MobilePhoneItemForm()
        return render(request, 'mobilephone/mobilephoneForm.html', {'af': af})
    def post(self, request):
        if request.method == 'POST':
            mobilePhoneItemForm = MobilePhoneItemForm(request.POST)
            if mobilePhoneItemForm.is_valid():
                mobilePhoneItemForm.save()
                return redirect('/mobilephone/mobilephoneController/')


class MobilePhoneItemFormUpdateView(View):
    def get(self, request, id):
        mobilePhoneItem = MobilePhoneItem.objects.get(id=id)
        af = MobilePhoneForm(instance=mobilePhoneItem)
        return render(request, 'mobilephone/mobilephoneForm.html', {'af': af})
    def post(self, request, id):
        if request.method == 'POST':
            mobilePhoneItem = MobilePhoneItem.objects.get(id=id)
            mobilePhoneItemForm = MobilePhoneItemForm(request.POST, instance=mobilePhoneItem)
            if mobilePhoneItemForm.is_valid():
                mobilePhoneItemForm.save()
                return redirect('/mobilephone/mobilephoneController/')


class MobilePhoneItemFormDeleteView(View):
    def get(self, request, id):
        mobilePhoneItem = MobilePhoneItem.objects.get(id=id)
        af = MobilePhoneItemForm(instance=mobilePhoneItem)
        return render(request, 'mobilephone/delete.html', {'af': af, 'item': mobilePhoneItem})
    def post(self, request, id):
        if request.method == 'POST':
            mobilePhoneItem = MobilePhoneItem.objects.get(id=id)
            mobilePhoneItem.delete()
            return redirect('/mobilephone/mobilephoneController/')

