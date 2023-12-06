from django.urls import path
from . import views

urlpatterns = [
    path('', views.edit_records, name="edit-records"),
    path('customer/<uuid:id>', views.edit_records_customer, name="edit-records-store"),
    path('product/<uuid:id>', views.edit_records_product, name="edit-records-customer"),
    path('store/<uuid:id>', views.edit_records_store, name="edit-records-store"),
    path('user/<uuid:id>', views.edit_records_user, name="edit-records-user"),
]