from django.urls import path
from . import views

app_name = 'clothes'
urlpatterns = [
    path('', views.ClothesABC.as_view(), name='clothes'),
    path('clothesController/', views.ClothesController.as_view(), name='clothesController'),
    path('typeClothesForm/', views.TypeClothesFormView.as_view(), name='typeClothesForm'),
    path('updateTypeClothesForm/<int:id>', views.TypeClothesFormUpdateView.as_view(), name='typeClothesFormUpdate'),
    path('deleteTypeClothesForm/<int:id>', views.TypeClothesFormDeleteView.as_view(), name='typeClothesFormDelete'),
    path('brandClothesForm/', views.BrandClothesFormView.as_view(), name='brandClothesForm'),
    path('updateBrandClothesForm/<int:id>', views.BrandClothesFormUpdateView.as_view(), name='brandClothesFormUpdate'),
    path('deleteBrandClothesForm/<int:id>', views.BrandClothesFormDeleteView.as_view(), name='brandClothesFormDelete'),
    path('clothesForm/', views.ClothesFormView.as_view(), name='clothesForm'),
    path('updateClothesForm/<int:id>', views.ClothesFormUpdateView.as_view(), name='clothesFormUpdate'),
    path('deleteClothesForm/<int:id>', views.ClothesFormDeleteView.as_view(), name='clothesFormDelete'),
    path('clothesItemForm/', views.ClothesItemFormView.as_view(), name='clothesItemForm'),
    path('updateClothesItemForm/<int:id>', views.ClothesItemFormUpdateView.as_view(), name='clothesItemFormUpdate'),
    path('deleteClothesItemForm/<int:id>', views.ClothesItemFormDeleteView.as_view(), name='clothesItemFormDelete'),
]
