from django.http import HttpResponse
import datetime
from django.template import Context, Template

def nacimiento(self):
    return HttpResponse("Hola, nací en el "+str(int(datetime.datetime.now().year)-int(20)))

def anio_de_nacimiento(self, edad):
    return (int(28/2/2002))

def probandoHTML(self):
    miHTML=open("C:/Users/agust/Desktop/MVT/PrimerProyecto/plantillas/template1.html")
    plantilla=Template(miHTML.read())
    miHTML.close()
    contexto=Context()
    documento=plantilla.render(contexto)
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