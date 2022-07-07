"""PrimerProyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from PrimerProyecto.views import saludar, segunda_vista, dia_de_hoy, nacimiento, probandoHTML

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludar, name='saludar'),
    path('segundavista/', segunda_vista, name='segunda_vista'),
    path('diadehoy/', dia_de_hoy),
    path('nacimiento/<edad>', nacimiento),
    path('probandoHTML', probandoHTML),
]
