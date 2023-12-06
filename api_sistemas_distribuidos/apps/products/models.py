from django.db import models
import uuid

# Create your models here.
class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=40, blank=False)
    category = models.CharField(max_length=30, blank=False)
    brand = models.CharField(max_length=30, blank=False)
    price = models.IntegerField(blank=False)
    stock = models.IntegerField(blank=False)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering =['id']

    def __str__(self):
        return self.title