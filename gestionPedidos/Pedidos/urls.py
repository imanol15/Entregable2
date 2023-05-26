from django.urls import path
from . import views


urlpatterns = [
    
    #Pagina Principal
    path('', views.index, name='index'),
     
    #Urls de clientes
    path('clientes/', views.ClienteListView.as_view(), name='listado_clientes'),
    path('clientes/<int:pk>/', views.ClienteDetailView.as_view(), name='cliente_detail'),
    path('clientes/<cliente_id>/pedido', views.show_pedido, name='cliente_pedido_detail'),
    path('clientes/create/', views.ClienteCreateView.as_view(), name='create_cliente'),
    path('clientes/<int:pk>/borrar/', views.ClienteDeleteView.as_view(), name='cliente_delete'),
    path('clientes/<int:pk>/editar/', views.ClienteUpdateView.as_view(), name='cliente_edit'),
    #Urls de pedidos
    path('pedidos/', views.PedidoListView.as_view(), name='listado_pedidos'),
    path('pedidos/<int:pk>', views.PedidoDetailView.as_view(), name='pedido_detail'),
    path('pedidos/create/', views.PedidoCreateView.as_view(), name='pedido_create'),
    path('pedidos/<int:pk>/borrar/', views.PedidoDeleteView.as_view(), name='pedido_delete'),
    path('pedidos/<int:pk>/editar/', views.PedidoUpdateView.as_view(), name='pedido_edit'),
    #Urls de componente
    path('componentes/', views.ComponenteListView.as_view(), name='listado_componentes'),
    path('componentes/<int:pk>', views.ComponenteDetailView.as_view(), name='componente_detail'),
    path('productos/<producto_id>/componente', views.show_producto, name='componente_producto_detail'),
    path('componentes/create/', views.ComponenteCreateView.as_view(), name='componente_create'),
    path('componentes/<int:pk>/borrar/', views.ComponenteDeleteView.as_view(), name='componente_delete'),
    path('componentes/<int:pk>/editar/', views.ComponenteUpdateView.as_view(), name='componente_edit'),
    path('api/componentes/<int:id>/', views.obtener_detalles_componente, name='api_componente'),

    #Urls de producto
    path('productos/', views.ProductoListView.as_view(), name='listado_productos'),
    path('productos/<int:pk>', views.ProductoDetailView.as_view(), name='producto_detail'),
    path('productos/create/', views.ProductoCreateView.as_view(), name='producto_create'),
    path('productos/<int:pk>/borrar/', views.ProductoDeleteView.as_view(), name='producto_delete'),
    path('productos/<int:pk>/editar/', views.ProductoUpdateView.as_view(), name='producto_edit'),
    #Urls de cantidad
    path('ProductoPedido/create/', views.ProductoPedidoCreateView.as_view(), name='ProductoPedido_create'), 
   
]





