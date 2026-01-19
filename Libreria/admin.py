from django.contrib import admin
from .models import Libreria, Empleado, Libro

# Register your models here.

admin.site.register(Libreria)
admin.site.register(Empleado)
admin.site.register(Libro)


