from django.db import models

# Create your models here.
class Curso(models.Model): 
    nombre = models.CharField(max_length=50)
    comision= models.IntegerField()

class Familia(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    anio_de_nacimiento=models.IntegerField() 
    edad=models.IntegerField() 