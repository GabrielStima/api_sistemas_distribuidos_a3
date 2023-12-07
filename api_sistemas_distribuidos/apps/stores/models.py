from django.db import models
import uuid

# Create your models here.
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