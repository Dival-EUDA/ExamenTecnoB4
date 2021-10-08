from django.shortcuts import render
from .models import *
# Create your views here.

def CRUD(request):

    return render(request, 'index.html')

def TABLES(request):
    empleado = Empleado.objects.all()
    return render(request, 'tables.html',{'empleado':empleado})

def FORM(request):
    return render(request, 'form-basic.html')

def FORM2(request):
    computer = Computador.objects.all()
    return render(request, 'form-wizard.html',{'computer':computer})