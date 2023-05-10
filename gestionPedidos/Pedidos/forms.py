from django.forms import ModelForm
from .models import Componente,Producto,Pedido,Cliente,ProductoPedido,ProductoComponente

class PedidoForm(ModelForm):
 class Meta:
    model = Pedido
    fields = ('codigo_referencia', 'fecha', 'cliente', 'preciototal')

class ComponenteForm(ModelForm):
 class Meta:
    model = Componente
    fields = '__all__'

class ProductoForm(ModelForm):
 class Meta:
    model = Producto
    fields = ('referencia', 'precio', 'nombre', 'descripcion','categoria')

class ClienteForm(ModelForm):
 class Meta:
    model = Cliente
    fields = '__all__'

class ProductoPedidoForm(ModelForm):
 class Meta:
    model = ProductoPedido
    fields = '__all__'

class ProductoComponenteForm(ModelForm):
   class Meta:
      model = ProductoComponente
      fields = '__all__'
