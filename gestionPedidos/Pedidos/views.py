
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Componente, Producto, Cliente, Pedido


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


    
class ComponenteListView(ListView):
    model = Componente
    template_name = 'componente_list.html'
    context_object_name = 'componentes'
    paginate_by = 10

class ComponenteDetailView(DetailView):
    model = Componente
    template_name = 'componente_detail.html'

class ComponenteCreateView(CreateView):
    model = Componente
    template_name = 'componente_form.html'
    fields = ['nombre', 'descripcion']
    success_url = reverse_lazy('componente_list')

class ComponenteUpdateView(UpdateView):
    model = Componente
    template_name = 'componente_form.html'
    fields = ['nombre', 'descripcion']
    success_url = reverse_lazy('componente_list')

class ComponenteDeleteView(DeleteView):
    model = Componente
    template_name = 'componente_confirm_delete.html'
    success_url = reverse_lazy('componente_list')

class ProductoListView(ListView):
    model = Producto
    template_name = 'producto_list.html'
    context_object_name = 'productos'
    paginate_by = 10

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'producto_detail.html'

class ProductoCreateView(CreateView):
    model = Producto
    template_name = 'producto_form.html'
    fields = ['nombre', 'precio', 'componentes']
    success_url = reverse_lazy('producto_list')

class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = 'producto_form.html'
    fields = ['nombre', 'precio', 'componentes']
    success_url = reverse_lazy('producto_list')

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'producto_confirm_delete.html'
    success_url = reverse_lazy('producto_list')

class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente_list.html'
    context_object_name = 'clientes'
    paginate_by = 10

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'cliente_detail.html'

class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'cliente_form.html'
    fields = ['nombre', 'email']
    success_url = reverse_lazy('cliente_list')

class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'cliente_form.html'
    fields = ['nombre', 'email']
    success_url = reverse_lazy('cliente_list')

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente_list')

class PedidoListView(ListView):
    model = Pedido
    template_name = 'pedido_list.html'
    context_object_name = 'pedidos'
    paginate_by = 10

class PedidoDetailView(DetailView):
    model = Pedido
    template_name = 'pedido_detail.html'

class PedidoCreateView(CreateView):
    model = Pedido
    template_name = 'pedido_form.html'
    fields = ['cliente', 'productos']
    success_url = reverse_lazy('pedido_list')

class PedidoUpdateView(UpdateView):
    model = Pedido
    template_name = 'pedido'
