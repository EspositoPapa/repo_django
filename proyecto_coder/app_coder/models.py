from django.db import models
from django.forms import CharField, DateField

# Create your models here.

class Curso(models.Model):
    nombre=models.CharField(max_length=40)#Caracteres(string corto)#
    camada=models.IntegerField()#Campo entero(int)#

class Profesor(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField(max_length=70)
    profesion= models.CharField(max_length=30)
    
class Estudiante(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField(max_length=70)

class Entregables(models.Model):
    nombre=models.CharField(max_length=30)
    fecha=models.DateField()
    entregado=models.BooleanField()

