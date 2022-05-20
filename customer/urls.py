from django.urls import path
from . import views

app_name = 'customer'
urlpatterns = [
    path('', views.LoginForm.as_view(), name='login'),
]
