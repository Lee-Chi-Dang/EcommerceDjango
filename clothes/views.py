from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.shortcuts import redirect

from .models import TypeClothes, BrandClothes, ClothesA, ClothesItem
from .forms import TypeClothesForm, BrandClothesForm, ClothesForm, ClothesItemForm

# Create your views here.
class ClothesABC(View):
    def get(self, request):
        clothesItemList = ClothesItem.objects.all()
        return render(request, 'clothes/clothes.html', {
            'clothesItemList': clothesItemList,
        })


class ClothesController(View):
    def get(self, request):
        typeClothesList = TypeClothes.objects.all()
        brandClothesList = BrandClothes.objects.all()
        clothesList = ClothesA.objects.all()
        clothesItemList = ClothesItem.objects.all()
        return render(request, 'clothes/clothesController.html', {
            'typeClothesList': typeClothesList,
            'brandClothesList': brandClothesList,
            'clothesList': clothesList,
            'clothesItemList': clothesItemList,
        })

#----------------------- TypeClothes ------------------------------
class TypeClothesFormView(View):
    def get(self, request):
        af = TypeClothesForm()
        return render(request, 'clothes/clothesForm.html', {'af': af})
    def post(self, request):
        if request.method == 'POST':
            typeClothesForm = TypeClothesForm(request.POST)
            if typeClothesForm.is_valid():
                typeClothesForm.save()
                return redirect('/clothes/clothesController')


class TypeClothesFormUpdateView(View):
    def get(self, request, id):
        typeClothes = TypeClothes.objects.get(id=id)
        af = TypeClothesForm(instance=typeClothes)
        return render(request, 'clothes/clothesForm.html', {'af': af})
    def post(self, request, id):
        if request.method == 'POST':
            typeClothes = TypeClothes.objects.get(id=id)
            typeClothesForm = TypeClothesForm(request.POST, instance=typeClothes)
            if typeClothesForm.is_valid():
                typeClothesForm.save()
                return redirect('/clothes/clothesController')


class TypeClothesFormDeleteView(View):
    def get(self, request, id):
        typeClothes = TypeClothes.objects.get(id=id)
        af = TypeClothesForm(instance=typeClothes)
        return render(request, 'clothes/delete.html', {'af': af, 'item': typeClothes})
    def post(self, request, id):
        if request.method == 'POST':
            typeClothes = TypeClothes.objects.get(id=id)
            typeClothes.delete()
            return redirect('/clothes/clothesController')


#----------------------- BrandClothes ------------------------------
class BrandClothesFormView(View):
    def get(self, request):
        af = BrandClothesForm()
        return render(request, 'clothes/clothesForm.html', {'af': af})
    def post(self, request):
        if request.method == 'POST':
            brandClothesForm = BrandClothesForm(request.POST)
            if brandClothesForm.is_valid():
                brandClothesForm.save()
                return redirect('/clothes/clothesController')


class BrandClothesFormUpdateView(View):
    def get(self, request, id):
        brandClothes = BrandClothes.objects.get(id=id)
        af = BrandClothesForm(instance=brandClothes)
        return render(request, 'clothes/clothesForm.html', {'af': af})
    def post(self, request, id):
        if request.method == 'POST':
            brandClothes = BrandClothes.objects.get(id=id)
            brandClothesForm = BrandClothesForm(request.POST, instance=brandClothes)
            if brandClothesForm.is_valid():
                brandClothesForm.save()
                return redirect('/clothes/clothesController')


class BrandClothesFormDeleteView(View):
    def get(self, request, id):
        brandClothes = BrandClothes.objects.get(id=id)
        af = BrandClothesForm(instance=brandClothes)
        return render(request, 'clothes/delete.html', {'af': af, 'item': brandClothes})
    def post(self, request, id):
        if request.method == 'POST':
            brandClothes = BrandClothes.objects.get(id=id)
            brandClothes.delete()
            return redirect('/clothes/clothesController')


#----------------------- Clothes ------------------------------
class ClothesFormView(View):
    def get(self, request):
        af = ClothesForm()
        return render(request, 'clothes/clothesForm.html', {'af': af})
    def post(self, request):
        if request.method == 'POST':
            clothesForm = ClothesForm(request.POST)
            if clothesForm.is_valid():
                clothesForm.save()
                return redirect('/clothes/clothesController')


class ClothesFormUpdateView(View):
    def get(self, request, id):
        clothes = ClothesA.objects.get(id=id)
        af = ClothesForm(instance=clothes)
        return render(request, 'clothes/clothesForm.html', {'af': af})
    def post(self, request, id):
        if request.method == 'POST':
            clothes = ClothesA.objects.get(id=id)
            clothesForm = ClothesForm(request.POST, instance=clothes)
            if clothesForm.is_valid():
                clothesForm.save()
                return redirect('/clothes/clothesController')


class ClothesFormDeleteView(View):
    def get(self, request, id):
        clothes = ClothesA.objects.get(id=id)
        af = ClothesForm(instance=clothes)
        return render(request, 'clothes/delete.html', {'af': af, 'item': clothes})
    def post(self, request, id):
        if request.method == 'POST':
            clothes = ClothesA.objects.get(id=id)
            clothes.delete()
            return redirect('/clothes/clothesController')


#----------------------- ClothesItem ------------------------------
class ClothesItemFormView(View):
    def get(self, request):
        af = ClothesItemForm()
        return render(request, 'clothes/clothesForm.html', {'af': af})
    def post(self, request):
        if request.method == 'POST':
            clothesItemForm = ClothesItemForm(request.POST)
            if clothesItemForm.is_valid():
                clothesItemForm.save()
                return redirect('/clothes/clothesController')


class ClothesItemFormUpdateView(View):
    def get(self, request, id):
        clothesItem = ClothesItem.objects.get(id=id)
        af = ClothesItemForm(instance=clothesItem)
        return render(request, 'clothes/clothesForm.html', {'af': af})
    def post(self, request, id):
        if request.method == 'POST':
            clothesItem = ClothesItem.objects.get(id=id)
            clothesItemForm = ClothesItemForm(request.POST, instance=clothesItem)
            if clothesItemForm.is_valid():
                clothesItemForm.save()
                return redirect('/clothes/clothesController')


class ClothesItemFormDeleteView(View):
    def get(self, request, id):
        clothesItem = ClothesItem.objects.get(id=id)
        af = ClothesItemForm(instance=clothesItem)
        return render(request, 'clothes/delete.html', {'af': af, 'item': clothesItem})
    def post(self, request, id):
        if request.method == 'POST':
            clothesItem = ClothesItem.objects.get(id=id)
            clothesItem.delete()
            return redirect('/clothes/clothesController')

