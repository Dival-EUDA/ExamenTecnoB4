from django.db import models

# Create your models here.

class Computador(models.Model):
    pk_computadora = models.AutoField(primary_key=True, null=False, blank=False)
    marca = models.CharField(max_length=50, null=False, blank=False)
    modelo = models.CharField(max_length=50, null=False, blank=False)
    precio = models.CharField(max_length=50, null=False, blank=False)
    date = models.CharField(max_length=50, null=False, blank=False)


class Empleado(models.Model):
    pk_empleado = models.AutoField(primary_key=True, null=False, blank=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    puesto = models.CharField(max_length=50, null=False, blank=False)
    fk_computadora = models.OneToOneField(Computador, null=False, blank=False,on_delete=models.CASCADE)
