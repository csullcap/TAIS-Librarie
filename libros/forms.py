from django.forms import ModelForm
from .models import Autor, Libro

class LibroForm(ModelForm):
    class Meta:
        model = Libro
        fields = ["titulo","autor","descripcion",]

class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = ["nombre","apellido","nacionalidad","biografia",]