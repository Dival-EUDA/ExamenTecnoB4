from django.urls import path
from .views import *
urlpatterns = [
    path('', CRUD, name='CRUD'),
]