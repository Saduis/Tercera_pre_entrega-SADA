from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name = "home"),
    path('libros/', libros, name = "libros"),
    path('autores/', autores, name = "autores"),
    path('lectores/', lectores, name = "lectores"),
    path('prestamos/', prestamos, name = "prestamos"),



    #___FORMULARIOS DE CARGA

    path('libroForm/', libroForm, name = "libroForm"),
    path('autorForm/', autorForm, name = "autorForm"),
    path('lectorForm/', lectorForm, name = "lectorForm"),
    path('prestamoForm/', prestamoForm, name = "prestamoForm"),


    #___BUSQUEDA
    path('buscarLibros', buscarLibros, name = "buscarLibros"),
    path('encontrarLibros', encontrarLibros, name = "encontrarLibros"),
]
