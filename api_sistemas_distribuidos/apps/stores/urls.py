from django.urls import path
from . import views

urlpatterns = [
    path('', views.listStores, name="stores"),
]