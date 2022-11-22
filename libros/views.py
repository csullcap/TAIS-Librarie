from django.shortcuts import render
from .forms import LibroForm, AutorForm

# Create your views here.

def libros(request):
    return render(request, 'libros.html')

def libros_crear(request):
    return render(request, 'crear-libro.html',{
        'form':LibroForm
    })

def autores(request):
    return render(request, 'autores.html')

def autores_crear(request):
    return render(request, 'crear-autor.html',{
        'form':AutorForm
    })
