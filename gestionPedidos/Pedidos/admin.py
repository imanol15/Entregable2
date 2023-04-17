from django.contrib import admin
from .models import Componente,Producto,Pedido,Cliente
admin.site.register(Componente)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(Cliente)