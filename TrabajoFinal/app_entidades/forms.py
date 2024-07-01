from django import forms


class LibroForm (forms.Form):
    nombre= forms.CharField(max_length=100, required=True, label="Título")
    autor= forms.CharField(max_length=50, required=True, label="Autor")
    anio_edicion= forms.IntegerField( required=False, label="Año de edicion")
    editorial= forms.CharField(max_length=50, required=False, label="Editorial")

class AutorForm (forms.Form):
    nombre = forms.CharField(max_length=50, required=True, label="Nombre")
    apellido = forms.CharField(max_length=50, required=True, label="Apellido")
    nacionalidad = forms.CharField(max_length=50, required=True, label="Nacionalidad")

class LectorForm (forms.Form):
    nombre = forms.CharField(max_length=50, required=True, label="Nombre")
    apellido = forms.CharField(max_length=50, required=True, label="Apellido")
    email = forms.EmailField(required=False)

class PrestamoForm (forms.Form):
    nombre= forms.CharField(max_length=100, required=True, label="Nombre")
    apellido= forms.CharField(max_length=50, required=True, label="Apellido")
    libro= forms.CharField(max_length=50, required=True, label="Libro")
    fecha_prestamo= forms.DateField( required=True, label="Fecha préstamo")

