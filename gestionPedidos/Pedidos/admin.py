from django.contrib import admin
from .models import Componente,Producto,Pedido,Cliente,ProductoPedido


admin.site.register(ProductoPedido)
admin.site.register(Componente)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(Cliente)


