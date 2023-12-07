from django.shortcuts import render
from .models import Store

# Create your views here.
def listStores(request):
    template_name = 'listStores/index.html'
    context = {"listStores":Store.objects.all()}
    
    for item in context['listStores']:
        item.link = f'../editRecords?type=store&id={item.id}'

    return render(request, template_name, context)