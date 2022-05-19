from django.urls import path
from . import views

app_name = 'home'
admin_name = 'admin'
urlpatterns = [
    path('', views.index, name='home'),
    path('adminpage/', views.adminpage, name='adminpage'),
]
