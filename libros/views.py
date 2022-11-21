from django.shortcuts import render
from .forms import LibroForm

# Create your views here.

def libros(request):
    return render(request, 'libros.html')

def libros_crear(request):
    return render(request, 'crear-libro.html',{
        'form':LibroForm
    })

def autores(request):
    return render(request, 'autores.html')
