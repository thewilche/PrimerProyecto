from django.db import models

class Familia(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    fecha_de_nacimiento=models.IntegerField() 
    edad=models.IntegerField() 