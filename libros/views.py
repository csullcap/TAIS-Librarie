from django.shortcuts import render,redirect
from .models import Autor, Libro
from .forms import LibroForm, AutorForm

# Create your views here.

def libros(request):
    return render(request, 'libros.html')

def libros_crear(request):
    return render(request, 'crear-libro.html',{
        'form':LibroForm
    })

def autores(request):
    # projects = list(Project.objects.values())
    autores = Autor.objects.all()
    return render(request, 'autores.html', {
        'autores': autores
    })


def autores_crear(request):    
    if request.method == 'GET':
        return render(request, 'crear-autor.html',{
        'form':AutorForm
        })
    else:
        Autor.objects.create(nombre = request.POST['nombre'],apellido = request.POST['apellido'],nacionalidad = request.POST['nacionalidad'], biografia =request.POST['biografia'])
        return redirect('/autores')

def autores_detalle(request, id):
    autores = Autor.objects.get(id = id)
    return render(request, 'detalle-autor.html',{
        'autor':autores
    })