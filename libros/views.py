from django.shortcuts import render,redirect
from .models import Autor, Libro
from .forms import LibroForm, AutorForm

# Create your views here.

def libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros.html', {
        'libros': libros
    })

def libros_crear(request):
    if request.method == 'GET':
        return render(request, 'crear-libro.html',{
        'form':LibroForm
        })
    else:
        autor = Autor.objects.get(id = request.POST['autor'])
        Libro.objects.create(
            nombre = request.POST['nombre'],
            autor = autor,
            descripcion = request.POST['descripcion'], 
            agno_publicacion =request.POST['agno_publicacion'],
            editorial =request.POST['editorial'],
            genero_literario =request.POST['genero_literario'],
            idioma =request.POST['idioma']
            )
        return redirect('/libros')

def libro_detalle(request, id):
    libro = Libro.objects.get(id = id)
    return render(request, 'detalle-libro.html',{
        'libro':libro
    })

def libro_eliminar(request, id):
    libro = Libro.objects.get(id = id)
    libro.delete()
    return redirect('/libros')
    
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

def autores_eliminar(request, id):
    autor = Autor.objects.get(id = id)
    autor.delete()
    return redirect('/autores')