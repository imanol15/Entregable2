from django.urls import path
from . import views


urlpatterns = [
     
    #Urls de clientes
    path('', views.ClienteListView.as_view(), name='listado_clientes'),
    path('clientes/<int:pk>/', views.ClienteDetailView.as_view(), name='cliente_detail'),
    path('clientes/create/', views.ClienteCreateView.as_view(), name='create_cliente'),
    path('clientes/<int:pk>/borrar/', views.ClienteDeleteView.as_view(), name='cliente_delete'),
    path('clientes/<int:pk>/editar/', views.ClienteUpdateView.as_view(), name='cliente_edit'),
    #Urls de pedidos
    path('pedidos/', views.PedidoListView.as_view(), name='listado_pedidos'),
    path('pedidos/<int:pk>', views.PedidoDetailView.as_view(), name='pedido_detail'),
    path('pedidos/create/', views.PedidoCreateView.as_view(), name='pedido_create'),
    path('pedidos/<int:pk>/borrar/', views.PedidoDeleteView.as_view(), name='pedido_delete'),
    path('pedidos/<int:pk>/editar/', views.PedidoUpdateView.as_view(), name='pedido_edit'),
   
   
    path('componente/<int:componente>/producto', views.ProductoListView.as_view(), name='listado_producto'),
    path('producto/<int:pk>', views.ProductoDetailView.as_view(), name='producto'),

    path('componente/', views.ComponenteListView.as_view(), name='listado_componente'),
    path('componente/<int:pk>/', views.ComponenteDetailView.as_view(), name='detail_componente'),



    
    
   

    
]




