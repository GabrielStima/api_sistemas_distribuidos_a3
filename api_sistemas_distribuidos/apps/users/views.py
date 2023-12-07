from django.shortcuts import render
from .models import User

# Create your views here.
def listUsers(request, id=None):
    template_name = 'listUsers/index.html'
    context = {"listUsers":User.objects.all()}
    
    for item in context['listUsers']:
        item.link = f'../editRecords?type=user&id={item.id}'

    return render(request, template_name, context)