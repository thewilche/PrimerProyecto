from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template, loader
from AppCoderhouse.models import Curso, Juegos
from AppCoderhouse.forms import Juegos_form
import datetime

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

def inicio(request):
    return render(request, 'AppCoderhouse/inicio.html')

def begin(request):
    return render(request, 'AppCoderhouse/begin.html')

def curso (self):
    curso= Curso(nombre='Django', comision=939393)
    curso.save()
    texto= f'Curso creado: {curso.nombre} {curso.comision}'
    return HttpResponse(texto)

def fin(request):
    return render(request, 'AppCoderhouse/fin.html')

def Juegos(request):
    return render(request,'AppCoderhouse/juegos.html')

def juegos_formulario(request):
    if (request.method=="POST"):
        form=Juegos_form(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            titulo=info["titulo"]
            lanzamiento=info["lanzamiento"]
            genero=info["genero"]
            game=Juegos(titulo=titulo, lanzamiento=lanzamiento, genero=genero)
            game.save()
            return render (request, "AppCoder/inicio.html")
    else:
        form=Juegos_form()
    return render(request, "AppCoderhouse/juegos_formulario.html", {"formulario":form})