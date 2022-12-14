"""tais_librarie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from libros import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('libros/', views.libros),
    path('libros/crear', views.libros_crear),
    path('libros/<int:id>', views.libro_detalle, name = 'detalle-libro'),
    path('libros/<int:id>/eliminar', views.libro_eliminar, name = 'eliminar-libro'),
    path('autores/', views.autores),
    path('autores/crear', views.autores_crear),
    path('autores/<int:id>', views.autores_detalle, name = 'detalle-autor'),
    path('autores/<int:id>/eliminar', views.autores_eliminar, name = 'eliminar-autor')
]
