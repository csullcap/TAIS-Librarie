from django.forms import ModelForm
from .models import Autor, Libro

class LibroForm(ModelForm):
    class Meta:
        model = Libro
        fields = [
            "nombre",
            "autor",
            "descripcion",
            "agno_publicacion",
            "editorial",
            "genero_literario",
            "idioma"
            ]
        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args,**kwargs)

        #     self.fields["nombre"].widget.attrs.update({
        #         'class':'form-control'
        #     })
        #     self.fields["genero_literario"].widget.attrs.update({
        #         'class':'form-control'
        #     })


class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = ["nombre","apellido","nacionalidad","biografia",]