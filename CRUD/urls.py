from django.urls import path
from .views import *
urlpatterns = [
    path('', CRUD, name='CRUD'),
    path('tables/', TABLES, name='tables'),
    path('formbasic/', FORM, name='form'),
    path('formwizard/', FORM2, name='formwizard'),
]