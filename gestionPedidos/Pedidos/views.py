
from .models import Producto, Pedido,Componente, Cliente
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views import View
from Pedidos.forms import PedidoForm, ClienteForm,ComponenteForm,ProductoForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy



class ProductoDetailView(ListView):
    model = Producto

class ProductoListView(DetailView):
    model = Producto
    context_object_name='productos'
    def get_queryset(self):
        self.componente = get_object_or_404(Componente,  pk=self.kwargs['Cmponente_id'])
        return Componente.objects.filter(Componente=self.componente)
        
        
    
    def get_context_data(self, **kwargs):
        # En primer lugar cogemos el contexto existente en la implementación base
        context = super().get_context_data(**kwargs)
        # En segundo lugar añadimos la información que queramos al contexto
        componente = get_object_or_404(Componente, pk=self.kwargs['componente_id'])
        context['componente'] = componente
        # Ejemplo de cómo añadir otra variable más al contexto de la template
        # usuario_conectado = 'Jaime Urrutia '
        # context['usuario_conectado'] = usuario_conectado
        return context
    
class ProductoCreateView(View):
    # Llamada para mostrar la página con el formulario de creación
    def get(self, request, *args, **kwargs):
        formulario = ProductoForm()
        context = {
            'formulario': formulario
        }
        return render(request, 'producto_create.html', context)

    # Llamada para procesar la creación del empleado
    def post(self, request, *args, **kwargs):
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():

            formulario.save()

            # Volvemos a la lista de departamentos
            return redirect('listado_producto')

        return render(request, 'producto_create.html', {'formulario': formulario})

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


class ComponenteCreateView(View):
    
    def get(self, request, *args, **kwargs):
        formulario = ComponenteForm()
        context = {
            'formulario': formulario
        }
        return render(request, 'componente_create.html', context)

    # Llamada para procesar la creación del departamento
    def post(self, request, *args, **kwargs):
        formulario = ComponenteForm(request.POST)
        if formulario.is_valid(): # is_valid() deja los datos validados en el atributo cleaned_data
       
            formulario.save()

            # Volvemos a la lista de departamentos
            return redirect('listado_componentes')
        # Si los datos no son válidos, mostramos el formulario nuevamente indicando los errores
        return render(request, 'componente_create.html', {'formulario': formulario})
    


# Vista mediante clase: igual que la vista anterior:
class ComponenteListView(View):
    def get(self, request):
        componentes = get_list_or_404(Componente.objects.order_by('componentes_codigo_referencia'))
        context = {'listado_componentes': componentes }
        return render(request, 'componente_list.html', context)

# Vista mediante clase: devuelve los datos de un departamento
class ComponenteDetailView(DetailView):
   model = Componente
