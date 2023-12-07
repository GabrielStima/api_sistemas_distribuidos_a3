from django.db import models
import uuid

# # Create your models here.
# class User(models.Model):
#     id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
#     firstname = models.CharField(max_length=30, blank=False)
#     lastname = models.CharField(max_length=50, blank=False)
#     email = models.EmailField(blank=False)
#     phone = models.BigIntegerField(blank=False)
#     birthdate = models.DateField(blank=False)
#     profile = models.CharField(max_length=20, blank=False)

#     class Meta:
#         verbose_name = 'Usuario'
#         verbose_name_plural = 'Usuarios'
#         ordering =['id']

#     def __str__(self):
#         return self.firstname
    
class Store(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=40, blank=False)
    cnpj = models.CharField(max_length=18, blank=False)
    address = models.CharField(max_length=60, blank=False)


    class Meta:
        verbose_name = 'Loja'
        verbose_name_plural = 'Lojas'
        ordering =['id']

    def __str__(self):
        return self.name
    
# class Product(models.Model):
#     id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
#     title = models.CharField(max_length=40, blank=False)
#     category = models.CharField(max_length=30, blank=False)
#     brand = models.CharField(max_length=30, blank=False)
#     price = models.IntegerField(blank=False)
#     stock = models.IntegerField(blank=False)

#     class Meta:
#         verbose_name = 'Produto'
#         verbose_name_plural = 'Produtos'
#         ordering =['id']

#     def __str__(self):
#         return self.title
    
# class Customer(models.Model):
#     id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
#     firstname = models.CharField(max_length=30, blank=False)
#     lastname = models.CharField(max_length=50, blank=False)
#     email = models.EmailField(blank=False)
#     phone = models.BigIntegerField(blank=False)
#     birthdate = models.DateField(blank=False)
    
#     class Meta:
#         verbose_name = 'Cliente'
#         verbose_name_plural = 'Clientes'
#         ordering =['id']

#     def __str__(self):
#         return self.firstname