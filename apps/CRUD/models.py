from django.db import models

# Create your models here.

class Computador(models.Model):
    pk_computadora = models.AutoField(primary_key=True, null=False, blank=False)
    marca = models.CharField(max_length=50, null=False, blank=False)
    modelo = models.CharField(max_length=50, null=False, blank=False)
    precio = models.CharField(max_length=50, null=False, blank=False)
    date = models.CharField(max_length=50, null=False, blank=False)
    uso = models.CharField(max_length=2, null=False, blank=False, default="0")


class Empleado(models.Model):
    pk_empleado = models.AutoField(primary_key=True, null=False, blank=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    puesto = models.CharField(max_length=50, null=False, blank=False)
    computadora = models.CharField(max_length=50, null=True, blank=True, default="null")
