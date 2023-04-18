from django.db import models
# ENtre las clases Componente y Producto hemos elegido que sea 1-n, es decir, un componente tiene varios Productos 
# y varios productos pueden tener el mismo componente, aunque tambien podria ser una n-m
#  que varios componentes sean de varios productos y viceversa
class Componente(models.Model):
    componentes_codigo_referencia = models.CharField(max_length=50, unique=True)
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
    pedido_codigo_referencia = models.CharField(max_length=50, unique=True)
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
# Hemos hecho una conexion n-m para producto pedido, es decir, varios pedidos pueden ser de varios productos y viceersa
class Producto_pedido(models.Model):
    producto_solicitado = models.ForeignKey(Producto, on_delete=models.CASCADE)
    producto_solicitado = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    


    

          
    