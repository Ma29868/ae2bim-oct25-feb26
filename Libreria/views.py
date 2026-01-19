from django.shortcuts import render
from .models import Libreria, Empleado, Libro
from .forms import LibreriaForm, EmpleadoForm, LibroForm

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'Libreria/home.html')

#Crear lista Librerias
def listar_librerias(request):
    librerias = Libreria.objects.all()
    return render(request, 'Libreria/listar_librerias.html', {
        'librerias': librerias
    })

#Crear Librerías
from .forms import LibreriaForm
from django.shortcuts import redirect

def crear_libreria(request):
    if request.method == 'POST':
        form = LibreriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_librerias')
    else:
        form = LibreriaForm()

    return render(request, 'Libreria/crear_libreria.html', {
        'form': form
    })

#Editar Librerías
from django.shortcuts import get_object_or_404

def editar_libreria(request, id):
    libreria = get_object_or_404(Libreria, id=id)

    if request.method == 'POST':
        form = LibreriaForm(request.POST, instance=libreria)
        if form.is_valid():
            form.save()
            return redirect('listar_librerias')
    else:
        form = LibreriaForm(instance=libreria)

    return render(request, 'Libreria/editar_libreria.html', {
        'form': form,
        'libreria': libreria
    })



#Crear Lista de Empleados
def listar_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'Libreria/listar_empleado.html', {
                  'empleados': empleados
                  })


#Crear Empleado 
from django.shortcuts import render, redirect
from .models import Empleado
from .forms import EmpleadoForm

def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_empleados')
    else:
        form = EmpleadoForm()

    return render(request, 'Libreria/crear_empleado.html', {
        'form': form
    })


#Editar Empleado
from django.shortcuts import get_object_or_404

def editar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)

    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('listar_empleado')
    else:
        form = EmpleadoForm(instance=empleado)

    return render(request, 'Libreria/editar_empleado.html', {
        'form': form,
        'empleado': empleado
    })


#Crear Lista de libro
def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'Libreria/listar_libros.html', {
                  'libros': libros
                  })


#Crear Libro 
from django.shortcuts import render, redirect
from .models import Libro
from .forms import LibroForm

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_libro')
    else:
        form = LibroForm()

    return render(request, 'Libreria/crear_libro.html', {
        'form': form
    })



#Editar Libro 
from django.shortcuts import get_object_or_404

def editar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)

    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('listar_libro')
    else:
        form = LibroForm(instance=Libro)

    return render(request, 'Libreria/editar_libro.html', {
        'form': form,
        'libro': libro
    })