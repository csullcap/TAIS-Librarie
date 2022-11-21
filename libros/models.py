from django.db import models
# Create your models here.



class Autor(models.Model):
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 100)

class Libro(models.Model):
    titulo = models.CharField(max_length = 100)
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE)
    descripcion = models.TextField(blank = True)