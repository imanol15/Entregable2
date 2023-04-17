from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/<int:referencia>/', views.detalle_producto, name='detalle_producto'),
    path('pedidos/', views.lista_pedidos, name='lista_pedidos'),
    path('pedidos/<int:Pedido_codigo_referencia>/', views.detalle_pedido, name='detalle_pedido'),
]