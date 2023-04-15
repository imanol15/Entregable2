from django.db import models

class Componente(models.Model):
    codigo_referencia = models.CharField(max_length=50, unique=True)
    nombre_modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)

class Producto(models.Model):
    referencia = models.CharField(max_length=50, unique=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=50)
    componentes = models.ManyToManyField(Componente)

class Pedido(models.Model):
    codigo_referencia = models.CharField(max_length=50, unique=True)
    fecha = models.DateField()
    cif_cliente = models.CharField(max_length=50)
    nombre_empresa_cliente = models.CharField(max_length=100)
    direccion_cliente = models.CharField(max_length=200)
    datos_contacto_cliente = models.CharField(max_length=200)
    producto_solicitado = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)