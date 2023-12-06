from django.shortcuts import render
import sys
# sys.path.insert("../customers")
# sys.path.insert("../stores")
# sys.path.insert("../users")
# sys.path.insert("../products")
from stores.models import Store
from products.models import Product
from users.models import User
from customers.models import Customer

array = {}

def template(object):
    global array
    array = dir(object)
    

def edit_records(request):
    template_name = 'editRecords/index.html'
    context = {}
    return render(request, template_name, context)

def edit_records_store(request, id=None):
    template_name = 'editRecords/index.html'
    context = {"item":Store.objects.get(id=id)}
    template(context['item'])
    # print(context['item'])
    print(context)
    return render(request, template_name, context)

def edit_records_product(request, id=None):
    template_name = 'editRecords/index.html'
    context = {"item":Product.objects.get(id=id)}
    return render(request, template_name, context)

def edit_records_customer(request):
    template_name = 'editRecords/index.html'
    context = {"item":Customer.objects.get(id=id)}
    return render(request, template_name, context)

def edit_records_user(request):
    template_name = 'editRecords/index.html'
    context = {"item":User.objects.get(id=id)}
    template(context['item'])
    return render(request, template_name, context)