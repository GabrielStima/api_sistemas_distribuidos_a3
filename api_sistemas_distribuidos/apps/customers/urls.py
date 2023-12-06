from django.urls import path
from . import views

urlpatterns = [
    path('', views.listCustomers, name="customers"),
]