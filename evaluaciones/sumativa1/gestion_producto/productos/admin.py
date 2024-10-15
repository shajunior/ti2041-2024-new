from django.contrib import admin
from .models import Categoria, Marca, Caracteristica, Producto

admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Caracteristica)
admin.site.register(Producto)
