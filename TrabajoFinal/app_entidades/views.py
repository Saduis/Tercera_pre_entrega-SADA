from django.shortcuts import render
from .forms import *
from app_entidades.models import *
from app_entidades.forms import *


# Create your views here.

def home(request):
    return render(request, "entidades/index.html")

def libros(request):
    contexto = {'libros': Libro.objects.all()}
    return render(request, "entidades/libros.html", contexto)

def autores(request):
    contexto = {'autores': Autor.objects.all()}
    return render(request, "entidades/autores.html", contexto)

def lectores(request):
    contexto = {'lectores': Lector.objects.all()}
    return render(request, "entidades/lectores.html", contexto)

def prestamos(request):
    contexto = {'prestamos': Prestamo.objects.all()}
    return render(request, "entidades/prestamos.html", contexto)


#___FUNCIONES

#___FORMULARIOS

def libroForm(request):
    if request.method == "POST":
        miForm = LibroForm(request.POST)
        if miForm.is_valid():
            nombre = miForm.cleaned_data.get("nombre")
            autor = miForm.cleaned_data.get("autor")
            anio_edicion = miForm.cleaned_data.get("anio_edicion")
            editorial = miForm.cleaned_data.get("editorial")

            libro = Libro(nombre=nombre, autor=autor, anio_edicion=anio_edicion, editorial=editorial) 
            libro.save()

            contexto = {"libros": Libro.objects.all()}

            return render(request, "entidades/libros.html", contexto)
    else:
        miForm = LibroForm()
    return render(request, "entidades/libroForm.html", {"form" : miForm})
    


def autorForm(request):
    if request.method == "POST":
        miForm = AutorForm(request.POST)
        if miForm.is_valid():
            nombre = miForm.cleaned_data.get("nombre")
            apellido = miForm.cleaned_data.get("apellido")
            nacionalidad = miForm.cleaned_data.get("nacionalidad")

            autor = Autor(nombre=nombre, apellido=apellido, nacionalidad=nacionalidad)
            autor.save()

            contexto = {"autores": Autor.objects.all()}

            return render(request, "entidades/autores.html", contexto)

    else:
        miForm = AutorForm()
    return render(request, "entidades/autorForm.html", {"form":miForm})

def lectorForm(request):
    if request.method == "POST":
        miForm = LectorForm(request.POST)
        if miForm.is_valid():
            nombre = miForm.cleaned_data.get("nombre")
            apellido = miForm.cleaned_data.get("apellido")
            email = miForm.cleaned_data.get("email")

            lector = Lector(nombre=nombre, apellido=apellido, email=email)
            lector.save()

            contexto = {"lectores": Lector.objects.all()}

            return render(request, "entidades/lectores.html", contexto)

    else:
        miForm = LectorForm()
    return render(request, "entidades/lectorForm.html", {"form":miForm})

def prestamoForm(request):
    if request.method == "POST":
        miForm = PrestamoForm(request.POST)
        if miForm.is_valid():
            nombre = miForm.cleaned_data.get("nombre")
            apellido = miForm.cleaned_data.get("apellido")
            libro = miForm.cleaned_data.get("libro")
            fecha_prestamo = miForm.cleaned_data.get("fecha_prestamo")

            prestamo = Prestamo(nombre=nombre, apellido=apellido, libro=libro, fecha_prestamo=fecha_prestamo)
            prestamo.save()

            contexto = {"prestamos": Prestamo.objects.all()}

            return render(request, "entidades/prestamos.html", contexto)

    else:
        miForm = PrestamoForm()
    return render(request, "entidades/prestamoForm.html", {"form":miForm})


#___BUSQUEDA

def buscarLibros(request):
    return render(request , "entidades/buscar.html") 

def encontrarLibros(request):
    if request.GET["buscar"]:
        patron= request.GET["buscar"]
        libros = Libro.objects.filter(nombre__icontains=patron )
        contexto = {'libros': libros}
    else:
        contexto = {'libros' : Libro.objects.all()}
    return render(request, "entidades/libros.html", contexto)