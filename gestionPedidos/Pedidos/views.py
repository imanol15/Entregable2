
from .models import Producto, Pedido,Componente, Cliente
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, get_list_or_404
from django.urls import path
from . import views



class ProductoListView(ListView):
    model = Producto

class ProductoDetailView(DetailView):
    model = Producto

class PedidoListView(ListView):
    model = Pedido

class PedidoDetailView(DetailView):
    model = Pedido
    context_object_name='pedidos'
    def get_queryset(self):
      self.cliente = get_object_or_404(Cliente,  pk=self.kwargs['cliente_id'])
      return Pedido.objects.filter(Cliente=self.cliente)



class ComponenteListView(ListView):
    model = Componente

class ComponenteDetailView(DetailView):
    model = Componente


    
urlpatterns = [
    # Paths para vistas utilizando FUNCIONES:

    # path('', views.index_departamentos, name='index'),
    # path('departamentos/<int:departamento_id>/', views.show_departamento, name='detail'),
    # path('departamentos/<int:departamento_id>/empleados', views.index_empleados, name='empleados'),
    # path('habilidades/<int:habilidad_id>', views.show_habilidad, name='habilidad'),
    
    # Paths para vistas utilizando CLASES:

    path('', views.DepartamentoListView.as_view(), name='index'),
    path('departamentos/<int:pk>/', views.DepartamentoDetailView.as_view(), name='detail'),
    path('departamentos/<int:departamento_id>/empleados', views.EmpleadoListView.as_view(), name='empleados'),
    path('empleados/<int:pk>', views.EmpleadoDetailView.as_view(), name='empleado'),
    path('habilidades/<int:pk>', views.HabilidadDetailView.as_view(), name='habilidad'),

    # Paths para crear
    path('departamentos/create', views.DepartamentoCreateView.as_view(), name='departamento_create'),
    path('empleados/create', views.EmpleadoCreateView.as_view(), name='empleado_create'),
]

    



