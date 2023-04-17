from django.db import models

class Componente(models.Model):
    Componentes_codigo_referencia = models.CharField(max_length=50, unique=True)
    nombre_modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=70)

class Producto(models.Model):
    referencia = models.CharField(max_length=50, unique=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=50)
    componentes = models.ForeignKey(Componente, on_delete=models.CASCADE)
    
class Cliente(models.Model):
    cif_cliente = models.CharField(max_length=50)
    nombre_empresa_cliente = models.CharField(max_length=100)
    direccion_cliente = models.CharField(max_length=200)
    datos_contacto_cliente = models.CharField(max_length=200)
    

class Pedido(models.Model):
    Pedido_codigo_referencia = models.CharField(max_length=50, unique=True)
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto_solicitado = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)

    

          
    