from django.urls import path
from . import views

app_name = 'mobilephone'
urlpatterns = [
    path('', views.MobilePhoneABC.as_view(), name='mobilephone'),
    path('mobilephoneController/', views.MobilephoneController.as_view(), name='mobilephoneController'),
    path('mobilephoneForm/', views.MobilePhoneFormView.as_view(), name='mobilephoneForm'),
    path('updateMobilephoneForm/<int:id>', views.MobilePhoneFormUpdateView.as_view(), name='mobilephoneFormUpdate'),
    path('deleteMobilephoneForm/<int:id>', views.MobilePhoneFormDeleteView.as_view(), name='mobilephoneFormDelete'),
    path('mobilephoneItemForm/', views.MobilePhoneItemFormView.as_view(), name='mobilephoneItemForm'),
    path('updateMobileItemphoneForm/<int:id>', views.MobilePhoneItemFormUpdateView.as_view(), name='mobilephoneItemFormUpdate'),
    path('deleteMobileItemphoneForm/<int:id>', views.MobilePhoneItemFormDeleteView.as_view(), name='mobilephoneItemFormDelete'),
]
