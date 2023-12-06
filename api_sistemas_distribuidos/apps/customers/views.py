from django.shortcuts import render
from .models import Customer

# Create your views here.
def listCustomers(request):
    template_name = 'listCustomers/index.html'
    context = {"listCustomers":Customer.objects.all()}
    
    for item in context['listCustomers']:
        item.link = f'../editRecords?type=customer&id={item.id}'

    return render(request, template_name, context)