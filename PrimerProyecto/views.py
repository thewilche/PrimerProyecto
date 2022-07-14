from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template, loader
from AppCoderhouse.models import Familia
import datetime

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
    ed=20
    naci=2002
    diccionario={'nombre':nom,'apellido':ape,'edad':ed,'nacimiento':naci}

    plantilla=Template(miArchivo.read())
    miArchivo.close()
    contexto=Context(diccionario)
    documento=plantilla.render(contexto)

    return HttpResponse(documento)