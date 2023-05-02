from django.contrib import admin
from .models import Componente,Producto,Pedido,Cliente,ProductoPedido

class ProductoPedidoInline(admin.TabularInline):
    model = ProductoPedido
    extra = 1

class PedidoAdmin(admin.ModelAdmin):
    inlines = [ProductoPedidoInline]
    list_display = ('codigo_referencia', 'fecha', 'cliente', 'preciototal', 'obtener_cantidades')

admin.site.register(Componente)
admin.site.register(Producto)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Cliente)


