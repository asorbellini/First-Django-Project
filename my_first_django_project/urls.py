"""
URL configuration for my_fistr_django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
#from myapp import urls # es lo mismo que hacer from myapp.views import hello, para importar todas las funciones de esa app. 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myapp.urls')) #Se puede agregar un url básico para que siempre que se desee acceder a un path sea necesario incluirlo, ejemplo poner "home/"
]
