from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template, loader
from AppCoderhouse.models import Curso, Familia
import datetime

def mama(self):
    mama=Familia(nombre='Cristina', apellido='Kirchner', fecha_de_nacimiento=str(int(datetime.datetime.now().year)-int(44)), edad=44)
    mama.save()
    texto=f'Me llamo {mama.nombre} {mama.apellido}, tengo {mama.edad} y nací en el {mama.fecha_de_nacimiento}.'
    return HttpResponse(texto)

def papa(self):
    papa=Familia(nombre='Ivan', apellido='Wilchepol', fecha_de_nacimiento=str(int(datetime.datetime.now().year)-int(48)), edad=48)
    papa.save()
    texto=f'Me llamo{papa.nombre} {papa.apellido}, tengo {papa.edad} y nací en el {papa.fecha_de_nacimiento}.'
    return HttpResponse(texto)

def abuelo(self):
    abuelo=Familia(nombre='Jorge', apellido='Wilchepol', fecha_de_nacimiento=str(int(datetime.datetime.now().year)-int(77)), edad=77)
    abuelo.save()
    texto=f'Me llamo{abuelo.nombre} {abuelo.apellido}, tengo {abuelo.edad} y nací en el {abuelo.fecha_de_nacimiento}.'
    return HttpResponse(texto)

def probandoHTML(self):
    miHTML=open("C:/Users/agust/Desktop/MVT/PrimerProyecto/plantillas/template1.html")
    plantilla=loader.get_Template(miHTML.read())
    miHTML.close()
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)

def probandoTemplate(self):
    miArchivo=open('C:/Users/agust/Desktop/MVT/PrimerProyecto/plantillas/template1.html')

    nom= 'Agustin'
    ape= 'Wilchepol'
    notas=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    diccionario={'nombre':nom,'apellido':ape,'lista':notas}

    plantilla=Template(miArchivo.read())
    miArchivo.close()
    contexto=Context(diccionario)
    documento=plantilla.render(contexto)

    return HttpResponse(documento)