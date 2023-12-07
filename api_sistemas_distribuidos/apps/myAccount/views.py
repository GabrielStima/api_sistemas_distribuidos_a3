from django.shortcuts import render

# Create your views here.
def my_account(request):
    template_name = 'myAccount/index.html'
    context = {}
    return render(request, template_name, context)