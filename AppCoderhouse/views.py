from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template, loader
from AppCoderhouse.models import Familia
import datetime

def mama(self):
    mama=Familia(nombre='Marcela', apellido='Genes', fecha_de_nacimiento=str(int(datetime.datetime.now().year)-int(44)), edad=44)
    
    texto=f'Me llamo {mama.nombre} {mama.apellido}, tengo {mama.edad} y nací en el {mama.fecha_de_nacimiento}.'
    return HttpResponse(texto)

def papa(self):
    papa=Familia(nombre='Ivan', apellido='Wilchepol', fecha_de_nacimiento=str(int(datetime.datetime.now().year)-int(48)), edad=48)
    
    texto=f'Me llamo {papa.nombre} {papa.apellido}, tengo {papa.edad} y nací en el {papa.fecha_de_nacimiento}.'
    return HttpResponse(texto)

def abuelo(self):
    abuelo=Familia(nombre='Jorge', apellido='Wilchepol', fecha_de_nacimiento=str(int(datetime.datetime.now().year)-int(77)), edad=77)
    
    texto=f'Me llamo {abuelo.nombre} {abuelo.apellido}, tengo {abuelo.edad} y nací en el {abuelo.fecha_de_nacimiento}.'
    return HttpResponse(texto)

def probandoHTML(self):
    miHTML=open("C:/Users/agust/Desktop/MVT/PrimerProyecto/plantillas/template1.html")
    nom= 'Agustin'
    ape= 'Wilchepol'
    ed=20
    naci=2002
    diccionario={'nombre':nom,'apellido':ape,'edad':ed,'nacimiento':naci}

    plantilla=Template(miHTML.read())
    miHTML.close()
    contexto=Context(diccionario)
    documento=plantilla.render(contexto)
    return HttpResponse(documento)

def probandoTemplate(self):
    miArchivo=open('C:/Users/agust/Desktop/MVT/PrimerProyecto/plantillas/template1.html')

    nom= 'Agustin'
    ape= 'Wilchepol'
    ed=20
    naci=2002
    diccionario={'nombre':nom,'apellido':ape,'edad':ed,'nacimiento':naci}

    plantilla=Template(miArchivo.read())
    miArchivo.close()
    contexto=Context(diccionario)
    documento=plantilla.render(contexto)

    return HttpResponse(documento)