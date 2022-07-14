from django.urls import path, include
from django.contrib import admin
from .views import *

urlpatterns = [
    path('probandoHTML/', probandoHTML),
    path('probandoTemplate/', probandoTemplate),
    path('curso/', curso),
    path('begin/', begin),
    path('fin/', fin),
    path('', inicio),
    path('Juegos/', Juegos, name='Juegos'),
    path('juegos_formularios/', juegos_formulario, name='juegos_formulario'),

]