from django.db import models
import uuid

# Create your models here.
class Customer(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    firstname = models.CharField(max_length=30, blank=False)
    lastname = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False)
    phone = models.BigIntegerField(blank=False)
    birthdate = models.DateField(blank=False)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering =['id']

    def __str__(self):
        return self.firstname