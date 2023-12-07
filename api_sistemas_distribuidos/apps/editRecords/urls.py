from django.urls import path
from . import views

urlpatterns = [
    path('', views.edit_records, name="edit-records"),
    path('customer/<uuid:id>', views.update_record_customer, name="update-records-store"),
    path('product/<uuid:id>', views.update_record_product, name="update-records-customer"),
    path('store/<uuid:id>', views.update_record_store, name="update-records-store"),
    path('user/<uuid:id>', views.update_record_user, name="update-records-user"),
]