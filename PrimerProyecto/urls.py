from django.contrib import admin
from django.urls import path, include
from AppCoderhouse import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppCoderhouse/', include('AppCoderhouse.urls')),
    

]
