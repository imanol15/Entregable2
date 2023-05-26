
from django.http import JsonResponse
from .models import Producto, Pedido,Componente, Cliente,ProductoPedido
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from Pedidos.forms import PedidoForm, ClienteForm,ComponenteForm,ProductoForm,ProductoPedidoForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

# LLamada a la pagina principal
def index(req):    
    return render(req,"index.html")

# Detalle de Pedidos
class PedidoDetailView(DetailView):
    model = Pedido
    template_name = 'pedido_detail.html'



# Listado de Pedidos
class PedidoListView(ListView):
    model = Pedido
    queryset = Pedido.objects.order_by('id')
    context_object_name = 'listado_pedidos'
    template_name = 'pedido_list.html'
    paginate_by = 3 

    def get_queryset(self):
        queryset = super().get_queryset()
        codigo_referencia_query = self.request.GET.get('codigo_referencia')

        if codigo_referencia_query:
            queryset = queryset.filter(codigo_referencia__icontains=codigo_referencia_query)

        return queryset
    
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
    fields = ['codigo_referencia', 'fecha', 'cliente', 'preciototal']




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
    queryset = Cliente.objects.order_by('id')
    context_object_name = 'listado_clientes'
    template_name = 'cliente_list.html'
    paginate_by = 3  
    
    def get_queryset(self):
        queryset = super().get_queryset()
        cif_query = self.request.GET.get('cif')

        if cif_query:
            queryset = queryset.filter(cif__icontains=cif_query)

        return queryset

    

# Detalle de cada Cliente
class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'cliente_detail.html'


#Borrado del cliente
class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = reverse_lazy('listado_clientes')
    template_name = 'cliente_delete.html'
#Actualizacion del cliente
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
    queryset = Componente.objects.order_by('id')
    context_object_name = 'listado_componentes'
    template_name = 'componente_list.html'
    paginate_by = 3 
    def get_queryset(self):
        queryset = super().get_queryset()
        componentes_codigo_referencia_query = self.request.GET.get('componentes_codigo_referencia')

        if componentes_codigo_referencia_query:
            queryset = queryset.filter(componentes_codigo_referencia__icontains=componentes_codigo_referencia_query)

        return queryset
    

# Detalle de cada Componente
class ComponenteDetailView(DetailView):
    model = Componente
    template_name = 'componente_detail.html'
#Borrado del componente
class ComponenteDeleteView(DeleteView):
    model = Componente
    success_url = reverse_lazy('listado_componentes')
    template_name = 'componente_delete.html'
#Actualizacion del componente
class ComponenteUpdateView(UpdateView):
    model = Componente
    template_name = 'componente_edit.html'
    success_url = reverse_lazy('listado_componentes')
    fields = ['componentes_codigo_referencia', 'nombre_modelo', 'marca']




# Detalle de productos
class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'producto_detail.html'

# Listado de Productos
class ProductoListView(ListView):
    model = Producto
    queryset = Producto.objects.order_by('id')
    context_object_name = 'listado_productos'
    template_name = 'producto_list.html'
    paginate_by = 3 

    def get_queryset(self):
        queryset = super().get_queryset()
        referencia_query = self.request.GET.get('referencia')

        if referencia_query:
            queryset = queryset.filter(referencia__icontains=referencia_query)

        return queryset
    
    
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
#Creacion ProductoPedido
class ProductoPedidoCreateView(CreateView):
    model = ProductoPedido
    form_class = ProductoPedidoForm
    template_name = 'productopedido_create.html'
    success_url = reverse_lazy('listado_pedidos')    

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)




def show_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    componente =  producto.componente_set.all()
    context = { 'producto': producto, 'listado_componente' : componente }
    return render(request, 'componente_list.html', context)


def show_pedido(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    pedido =  cliente.pedido_set.all()
    context = { 'cliente': cliente, 'listado_pedidos' : pedido }
    return render(request, 'pedido_list.html', context)

def obtener_detalles_componente(request, id):
    try:
        componente = Componente.objects.get(id=id)
        detalles = {
            'id': id,
            'codigo_referencia': componente.componentes_codigo_referencia,
            'modelo': componente.nombre_modelo,
            'marca': componente.marca,
        }
        return JsonResponse(detalles)
    except Componente.DoesNotExist:
        return JsonResponse({'error': 'El componente no existe'}, status=404)