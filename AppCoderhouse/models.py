from django.db import models
import datetime

# Create your models here.

'''class Familia(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    fecha_de_nacimiento=models.IntegerField() 
    edad=models.IntegerField()'''

class Curso(models.Model):
    nombre=models.CharField(max_length=50)
    comision=models.IntegerField()

class Juegos(models.Model):
    titulo=models.CharField(max_length=60)
    lanzamiento=models.DateField()
    genero=models.CharField(max_length=20)