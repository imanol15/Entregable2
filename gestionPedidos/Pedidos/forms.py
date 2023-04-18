from django.forms import ModelForm
from .models import Componente,Producto,Pedido,Cliente,Producto_pedido

class PedidoForm(ModelForm):
 class Meta:
    model = Pedido
    fields = '__all__'

class ComponenteForm(ModelForm):
 class Meta:
    model = Componente
    fields = '__all__'

class ProductoForm(ModelForm):
 class Meta:
    model = Producto
    fields = '__all__'

class ClienteForm(ModelForm):
 class Meta:
    model = Cliente
    fields = '__all__'

class Producto_pedidoForm(ModelForm):
 class Meta:
    model = Producto_pedido
    fields = '__all__'
