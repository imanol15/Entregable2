
from .models import Producto, Pedido,Componente, Cliente
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views import View
from Pedidos.forms import PedidoForm, ClienteForm,ComponenteForm,ProductoForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


# Detalle de Pedidos
class PedidoDetailView(DetailView):
    model = Pedido
    template_name = 'pedido_detail.html'

# Listado de Pedidos
class PedidoListView(ListView):
    model = Pedido
    queryset = Pedido.objects.order_by('codigo_referencia')
    context_object_name = 'listado_pedidos'
    template_name = 'pedido_list.html'
    
    
#Creacion Pedidos
class PedidoCreateView(CreateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'pedido_create.html'
    success_url = reverse_lazy('listado_pedidos')    

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
#Borrado de los pedidos
class PedidoDeleteView(DeleteView):
    model = Pedido
    success_url = reverse_lazy('listado_pedidos')
    template_name = 'pedido_delete.html'
#Actualizar pedidos
class PedidoUpdateView(UpdateView):
    model = Pedido
    template_name = 'pedido_edit.html'
    success_url = reverse_lazy('listado_pedidos')
    fields = ['codigo_referencia', 'fecha', 'cliente', 'cantidad']




# Creacion de clientes 
class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente_create.html'
    success_url = reverse_lazy('listado_clientes')    

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    


# Listado de Clientes
class ClienteListView(ListView):
    model = Cliente
    queryset = Cliente.objects.order_by('cif')
    context_object_name = 'listado_clientes'
    template_name = 'cliente_list.html'
    

# Detalle de cada Cliente
class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'cliente_detail.html'

class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = reverse_lazy('listado_clientes')
    template_name = 'cliente_delete.html'

class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'cliente_edit.html'
    success_url = reverse_lazy('listado_clientes')
    fields = ['cif', 'nombre_empresa', 'direccion', 'datos_contacto']

   
   
# Creacion de clientes 
class ComponenteCreateView(CreateView):
    model = Componente
    form_class = ComponenteForm
    template_name = 'componente_create.html'
    success_url = reverse_lazy('listado_componentes')    

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    


# Listado de Componente
class ComponenteListView(ListView):
    model = Componente
    queryset = Componente.objects.order_by('componentes_codigo_referencia')
    context_object_name = 'listado_componentes'
    template_name = 'componente_list.html'
    

# Detalle de cada Componente
class ComponenteDetailView(DetailView):
    model = Componente
    template_name = 'componente_detail.html'

class ComponenteDeleteView(DeleteView):
    model = Componente
    success_url = reverse_lazy('listado_componente')
    template_name = 'componente_delete.html'

class ComponenteUpdateView(UpdateView):
    model = Componente
    template_name = 'componente_edit.html'
    success_url = reverse_lazy('listado_componentes')
    fields = ['  componentes_codigo_referencia ', ' nombre_modelo', ' marca']




# Detalle de productos
class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'producto_detail.html'

# Listado de Productos
class ProductoListView(ListView):
    model = Producto
    queryset = Producto.objects.order_by('referencia')
    context_object_name = 'listado_productos'
    template_name = 'producto_list.html'
    
    
#Creacion Productos
class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto_create.html'
    success_url = reverse_lazy('listado_productos')    

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
#Borrado de los Productos
class ProductoDeleteView(DeleteView):
    model = Producto
    success_url = reverse_lazy('listado_productos')
    template_name = 'producto_delete.html'
#Actualizar productos
class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = 'producto_edit.html'
    success_url = reverse_lazy('listado_productos')
    fields = ['referencia', 'precio', 'nombre', 'descripcion','categoria','componentes']


