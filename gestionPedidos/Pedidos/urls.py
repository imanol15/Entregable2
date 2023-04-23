from django.urls import path
from . import views


urlpatterns = [
     

    path('', views.ClienteListView.as_view(), name='listado_clientes'),
    path('cliente/<int:pk>/', views.ClienteDetailView.as_view(), name='detail_componente'),
    path('clientes/<int:cliente_id>/pedidos', views.PedidoListView.as_view(), name='listado_pedidos'),
    path('pedidos/<int:pk>', views.PedidoDetailView.as_view(), name='pedido'),

    path('componente/<int:componente>/producto', views.ProductoListView.as_view(), name='listado_producto'),
    path('producto/<int:pk>', views.PedidoDetailView.as_view(), name='producto'),

    path('componente/', views.ComponenteListView.as_view(), name='listado_componente'),
    path('componente/<int:pk>/', views.ClienteDetailView.as_view(), name='detail_componente'),

    
    
   

    # Paths para crear
    path('clientes/create', views.ClienteCreateView.as_view(), name='cliente_create'),
    path('pedidos/create', views.PedidoCreateView.as_view(), name='pedido_create'),
    path('producto/create', views.ProductoCreateView.as_view(), name='producto_create'),
    path('componente/create', views.ComponenteCreateView.as_view(), name='componente_create'),
]




