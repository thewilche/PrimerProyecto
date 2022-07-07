from django.http import HttpResponse
import datetime
from django.template import Context, Template

def saludar(request):
    return HttpResponse('HELLO WORLD! \n COMO ESTAS?')

def segunda_vista(request):
    return HttpResponse('Espero que bien!\n ESTO ES MUY SIMPLE')

def dia_de_hoy(request):
    dia=datetime.datetime.today()
    codigodehtml = 'Hoy es: '+str(dia)
    return HttpResponse(codigodehtml)

def nacimiento(self, edad):
    return HttpResponse('<h2>Tu fecha de nacimiento es '+ str(int(datetime.datetime.now().year)-int(edad))+'<h2>')

def anio_de_nacimiento(self, edad):
    return str(int(datetime.datetime.now().year)-int(edad))

def probandoHTML(self):
    miHTML=open("C:/Users/agust/Desktop/MVT/PrimerProyecto/plantillas/template1.html")
    plantilla=Template(miHTML.read())
    miHTML.close()
    contexto=Context()
    documento=plantilla.render(contexto)
    return HttpResponse(documento)

def probandoTemplate(self):
    
    nombre= 'Agus'
    ape= 'Wilche'
    notas=[1,2,3,4,5,6,7,8,9,10]
    diccionario={'nombre':nombre,'apellido':ape,'lista':notas}

    plantilla=loader.get_template('template1.html')

    documento=plantilla.render(diccionario)
    return HttpResponse(documento)