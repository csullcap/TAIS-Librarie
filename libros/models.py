from django.db import models
# Create your models here.
from datetime import datetime   

generos_literarios = [
    (1,"Narrativa"),
    (2,"Lírica"),
    (3,"Dramática")
]

class Autor(models.Model):
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 100)
    nacionalidad = models.CharField(max_length = 100,blank = True)
    biografia = models.TextField(blank = True)

    def nombre_completo(self):
        return "{}, {}".format(self.apellido, self.nombre)
    def __str__(self):
        return self.nombre_completo()

class Libro(models.Model):
    nombre = models.CharField(default = "Nombre Libro", max_length = 100, verbose_name = 'Nombre')
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE, verbose_name = 'Autor')
    descripcion = models.TextField(default = "Descripción", blank = True, verbose_name = 'Descripción')
    agno_publicacion = models.DateField(default=datetime.now, blank=True, verbose_name = 'Año de publicación')
    editorial = models.CharField(default = "Editorial", max_length = 100, blank = True, verbose_name = 'Editorial')
    genero_literario = models.IntegerField(
        null = False , blank = False, choices = generos_literarios, default = 1, verbose_name = 'Género Literario' )
    idioma = models.CharField(max_length = 20, blank = True, verbose_name = 'Idioma')
