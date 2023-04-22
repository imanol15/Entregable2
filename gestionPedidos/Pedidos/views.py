
from .models import Producto, Pedido,Componente, Cliente
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views import View
from Pedidos.forms import PedidoForm, ClienteForm,ComponenteForm,ProductoForm
from django.shortcuts import render, redirect



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

        return render(request, 'producto_crete.html', {'formulario': formulario})

class PedidoDetailView(ListView):
    model = Pedido

class PedidoListView(DetailView):
    model = Pedido
    context_object_name='pedidos'
    def get_queryset(self):
        self.cliente = get_object_or_404(Cliente,  pk=self.kwargs['cliente_id'])
        return Pedido.objects.filter(Cliente=self.cliente)
        
        
    
    def get_context_data(self, **kwargs):
        # En primer lugar cogemos el contexto existente en la implementación base
        context = super().get_context_data(**kwargs)
        # En segundo lugar añadimos la información que queramos al contexto
        cliente = get_object_or_404(Cliente, pk=self.kwargs['cliente_id'])
        context['cliente'] = cliente
        # Ejemplo de cómo añadir otra variable más al contexto de la template
        # usuario_conectado = 'Jaime Urrutia '
        # context['usuario_conectado'] = usuario_conectado
        return context
    
class PedidoCreateView(View):
    # Llamada para mostrar la página con el formulario de creación
    def get(self, request, *args, **kwargs):
        formulario = PedidoForm()
        context = {
            'formulario': formulario
        }
        return render(request, 'pedido_create.html', context)

    # Llamada para procesar la creación del empleado
    def post(self, request, *args, **kwargs):
        formulario = PedidoForm(request.POST)
        if formulario.is_valid():

            formulario.save()

            # Volvemos a la lista de departamentos
            return redirect('listado_clientes')

        return render(request, 'pedido_create.html', {'formulario': formulario})




    



class ClienteCreateView(View):
    # Llamada para mostrar la página con el formulario de creación al usuario
    def get(self, request, *args, **kwargs):
        formulario = ClienteForm()
        context = {
            'formulario': formulario
        }
        return render(request, 'cliente_create.html', context)

    # Llamada para procesar la creación del departamento
    def post(self, request, *args, **kwargs):
        formulario = ClienteForm(request.POST)
        if formulario.is_valid(): # is_valid() deja los datos validados en el atributo cleaned_data
       
            formulario.save()

            # Volvemos a la lista de departamentos
            return redirect('listado_cliente')
        # Si los datos no son válidos, mostramos el formulario nuevamente indicando los errores
        return render(request, 'cliente_create.html', {'formulario': formulario})
    


# Vista mediante clase: igual que la vista anterior:
class ClienteListView(View):
    def get(self, request):
        clientes = get_list_or_404(Cliente.objects.order_by('cif'))
        context = {'listado_clientes': clientes }
        return render(request, 'cliente_list.html', context)

# Vista mediante clase: devuelve los datos de un departamento
class ClienteDetailView(DetailView):
   model = Cliente




class ComponenteCreateView(View):
    # Llamada para mostrar la página con el formulario de creación al usuario
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
