from django.urls import path
from . import views


urlpatterns = [
     

    path('', views.ClienteListView.as_view(), name='listado_clientes'),
    path('cliente/<int:pk>/', views.ClienteDetailView.as_view(), name='detail'),
    path('clientes/<int:departamento_id>/pedidos', views.PedidoListView.as_view(), name='listado_pedidos'),
    path('pedidos/<int:pk>', views.PedidoDetailView.as_view(), name='pedido'),
   

    # Paths para crear
    path('clientes/create', views.ClienteCreateView.as_view(), name='cliente_create'),
    path('pedidos/create', views.PedidoCreateView.as_view(), name='pedido_create'),
]




