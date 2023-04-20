
from .models import Producto, Pedido,Componente, Cliente
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, get_list_or_404



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

    



