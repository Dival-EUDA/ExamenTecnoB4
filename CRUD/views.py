from django.shortcuts import render

# Create your views here.

def CRUD(request):
    return render(request, 'index.html')

