from django import forms
from .models import Libreria, Empleado, Libro

#Libreria
class LibreriaForm(forms.ModelForm):
    class Meta:
        model = Libreria
        fields = ['nombre_libreria', 'direccion_fisica', 'numero_estantes']


#Empleado
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre_completo', 'cargo_empleado', 'salario_mensual', 'libreria']


#Libro
class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo_libro', 'autor_principal', 'genero_literario', 'precio_venta', 'numero_paginas']