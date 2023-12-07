from django.shortcuts import render
from .models import Product

# Create your views here.
def listProducts(request):
    template_name = 'listProducts/index.html'
    context = {"listProducts":Product.objects.all()}
    
    for item in context['listProducts']:
        item.link = f'../editRecords?type=product&id={item.id}'

    return render(request, template_name, context)