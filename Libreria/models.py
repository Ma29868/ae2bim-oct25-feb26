from django.db import models

# Create your models here.

class Libreria(models.Model):
    nombre_libreria = models.CharField(max_length=100, 
                    unique=True, 
                    null=False, 
                    blank=False
                    )
    direccion_fisica = models.CharField(max_length=50)
    numero_estantes = models.IntegerField()

    def __str__(self):
        return self.nombre_libreria
 



class Empleado(models.Model):
    nombre_completo = models.CharField(max_length=100)
    cargo_empleado = models.CharField(max_length=25)
    salario_mensual = models.DecimalField(max_digits=10, decimal_places=2)

    libreria = models.ForeignKey(
        Libreria,
        on_delete=models.CASCADE,
        related_name='empleados'
    )

    def __str__(self):
        return self.nombre_completo
  

    
class Libro(models.Model):
    titulo_libro = models.CharField(max_length=100)
    autor_principal = models.CharField(max_length=100)
    genero_literario = models.CharField(max_length=50)
    precio_venta = models.DecimalField(max_digits=4, decimal_places=2)
    numero_paginas = models.IntegerField()

    empleado = models.ForeignKey(
        Empleado,
        on_delete=models.CASCADE,
        related_name='libros'
    )

    def __str__(self):
        return self.titulo_libro
    
