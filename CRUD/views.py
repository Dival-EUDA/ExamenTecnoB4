from django.shortcuts import render

# Create your views here.

def CRUD(request):
    return render(request, 'index.html')

def TABLES(request):
    return render(request, 'tables.html')

def FORM(request):
    return render(request, 'form-basic.html')

def FORM2(request):
    return render(request, 'form-wizard.html')