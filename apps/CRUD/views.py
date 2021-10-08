from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def CRUD(request):

    return render(request, 'index.html')

def TABLES(request):
    empleado = Empleado.objects.all()
    return render(request, 'tables.html',{'empleado':empleado})

def FORM(request):
    if request.method == "POST":
        Marca = request.POST.get('marca')
        Modelo = request.POST.get('modelo')
        Precio = request.POST.get('precio')
        Date = request.POST.get('date')
        model_computer = Computador(marca=Marca,
                                    modelo=Modelo,
                                    precio=Precio,
                                    date=Date)
        model_computer.save()
        return redirect('CRUD:FORM')
    elif request.method == 'GET':
        return render(request, 'form-basic.html')

def FORM2(request):
    computer = Computador.objects.all()
    if request.method == "POST":
        Name = request.POST.get('name')
        Surname = request.POST.get('surname')
        Position = request.POST.get('position')
        ComputerU = request.POST.get('computer')



    return render(request, 'form-wizard.html',{'computer':computer})