from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('addcart', views.addcart, name='addcart'),
    path('shoppingcart', views.shoppingcart, name='shoppingcart'),
]
