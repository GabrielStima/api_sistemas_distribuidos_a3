from django.http import HttpResponse
from django.shortcuts import render
import json
from stores.models import Store
from products.models import Product
from users.models import User
from customers.models import Customer

objectInstance = {}

def formatDate(date):
    date_string = date
    date_parts = date_string.split(" ")
    day, month, year = date_parts[0], date_parts[2], date_parts[4]

    month_mapping = {
    "Janeiro": "01",
    "Fevereiro": "02",
    "Março": "03",
    "Abril": "04",
    "Maio": "05",
    "Junho": "06",
    "Julho": "07",
    "Agosto": "08",
    "Setembro": "09",
    "Outubro": "10",
    "Novembro": "11",
    "Dezembro": "12"
}

    day_mapping = {
        '1':'01',
        '2':'02',
        '3':'03',
        '4':'04',
        '5':'05',
        '6':'06',
        '7':'07',
        '8':'08',
        '9':'09',
    }

    month_number = month_mapping[month]
    final_date = ""

    if(int(day) < 10):
        day_number = day_mapping[day]
        final_date = f"{year}{month_number}{day_number}"
    else:
        final_date = f"{year}{month_number}{day}"

    return final_date

def template(type, object):
    array = []
    
    if type == 'store':
        propertys = [
            {'propertyName': 'name', 'propertyTitle': 'Nome'},
            {'propertyName': 'cnpj', 'propertyTitle': 'CNPJ'},
            {'propertyName': 'address', 'propertyTitle': 'Endereço'}
        ]

        for property in propertys:
            array.append({'property': property['propertyName'], 'value': getattr(object, property['propertyName']), 'title':  property['propertyTitle']})
        
        return array
        

    if type == 'user':
        propertys = [
            {'propertyName': 'firstname', 'propertyTitle': 'Nome'},
            {'propertyName': 'lastname', 'propertyTitle': 'Sobrenome'},
            {'propertyName': 'email', 'propertyTitle': 'Email'},
            {'propertyName': 'phone', 'propertyTitle': 'Telefone'},
            {'propertyName': 'birthdate', 'propertyTitle': 'Data de Nascimento'},
            {'propertyName': 'profile', 'propertyTitle': 'Perfil'},
        ]

        for property in propertys:
            array.append({'property': property['propertyName'], 'value': getattr(object, property['propertyName']), 'title':  property['propertyTitle']})
        
        return array


    if type == 'customer':
        propertys = [
            {'propertyName': 'firstname', 'propertyTitle': 'Nome'},
            {'propertyName': 'lastname', 'propertyTitle': 'Sobrenome'},
            {'propertyName': 'email', 'propertyTitle': 'Email'},
            {'propertyName': 'phone', 'propertyTitle': 'Telefone'},
            {'propertyName': 'birthdate', 'propertyTitle': 'Data de Nascimento'},
        ]

        for property in propertys:
            array.append({'property': property['propertyName'], 'value': getattr(object, property['propertyName']), 'title':  property['propertyTitle']})
        
        return array


    if type == 'product':
        propertys = [
            {'propertyName': 'title', 'propertyTitle': 'Nome'},
            {'propertyName': 'category', 'propertyTitle': 'Categoria'},
            {'propertyName': 'brand', 'propertyTitle': 'Marca'},
            {'propertyName': 'price', 'propertyTitle': 'Preço'},
            {'propertyName': 'stock', 'propertyTitle': 'Estoque'}
        ]

        for property in propertys:
            array.append({'property': property['propertyName'], 'value': getattr(object, property['propertyName']), 'title':  property['propertyTitle']})
        
        return array

def edit_records(request):
    global objectInstance
    type = request.GET.get('type', '')
    id = request.GET.get('id', '')
    context = {}
    template_name = 'editRecords/index.html'

    if type == 'store':
        objectInstance = Store.objects.get(id=id)
        context = {"fields":template("store", objectInstance)}

    if type == 'user':
        objectInstance = User.objects.get(id=id)
        context = {"fields":template("user", objectInstance)}

    if type == 'customer':
        objectInstance = Customer.objects.get(id=id)
        context = {"fields":template("customer", objectInstance)}

    if type == 'product':
        objectInstance = Product.objects.get(id=id)
        context = {"fields":template("product", objectInstance)}

    return render(request, template_name, context)
    
def update_record_store(request, id=None):
    global objectInstance
    data = json.loads(request.body)

    objectInstance.name = data['name']
    objectInstance.cnpj = data['cnpj']
    objectInstance.address = data['address']

    try:
        objectInstance.save()
        return HttpResponse(status=200)
    except:
        return HttpResponse(status=400)    

def update_record_product(request, id=None):
    global objectInstance
    data = json.loads(request.body)

    objectInstance.title = data['title']
    objectInstance.category = data['category']
    objectInstance.brand = data['brand']
    objectInstance.price = data['price']
    objectInstance.stock = data['stock']

    try:
        objectInstance.save()
        return HttpResponse(status=200)
    except:
        return HttpResponse(status=400)

def update_record_customer(request, id=None):
    global objectInstance
    data = json.loads(request.body)

    objectInstance.firstname = data['firstname']
    objectInstance.lastname = data['lastname']
    objectInstance.email = data['email']
    objectInstance.phone = data['phone']
    objectInstance.birthdate = formatDate(data['birthdate'])

    objectInstance.save()
    try:
        return HttpResponse(status=200)
    except:
        return HttpResponse(status=400)

def update_record_user(request, id=None):
    global objectInstance
    data = json.loads(request.body)

    objectInstance.firstname = data['firstname']
    objectInstance.lastname = data['lastname']
    objectInstance.email = data['email']
    objectInstance.phone = data['phone']
    objectInstance.birthdate = formatDate(data['birthdate'])
    objectInstance.profile = data['profile']

    try:
        objectInstance.save()
        return HttpResponse(status=200)
    except:
        return HttpResponse(status=400)
