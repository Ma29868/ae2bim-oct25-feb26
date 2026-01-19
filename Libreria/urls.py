from django.urls import path

from .views import (
    home,
    listar_librerias, crear_libreria, editar_libreria, 
    listar_empleados, crear_empleado, editar_empleado, 
    listar_libros, crear_libro, editar_libro
    )

urlpatterns = [
    #Home
    path('', home, name='home'),
    path('home/', home, name='home'),

    #Librerias
    path('librerias/', listar_librerias, name='listar_librerias'),
    path('librerias/crear/', crear_libreria, name='crear_libreria'),
    path('librerias/editar/<int:id>/', editar_libreria, name='editar_libreria'),

    #Empleados
    path('empleados/', listar_empleados, name='listar_empleados'),
    path('empleados/crear/', crear_empleado, name='crear_empleado'),
    path('empleados/editar/<int:id>/', editar_empleado, name='editar_empleado'),

    #Libros
    path('libros/', listar_libros, name='listar_libros'),
    path('libros/crear/', crear_libro, name='crear_libro'),
    path('libros/editar/<int:id>/', editar_libro, name='editar_libro'),

]


