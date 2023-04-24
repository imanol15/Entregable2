from django.db import models
# Entre las clases Componente y Producto hemos elegido que tenga una relación 1-n, es decir, un componente tiene varios Productos 
# y varios productos pueden tener el mismo componente, aunque tambien podria dependiendo de quien lo piense puede ser una n-m
# que varios componentes sean de varios productos y viceversa.
class Componente(models.Model):
    componentes_codigo_referencia = models.CharField(max_length=50, unique=True)
    nombre_modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=70)
    def __str__(self):
        return self.nombre_modelo


class Producto(models.Model):
    referencia = models.CharField(max_length=50, unique=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=50)
    componentes = models.ForeignKey(Componente, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    
class Cliente(models.Model):
    cif = models.CharField(max_length=50)
    nombre_empresa = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    datos_contacto = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre_empresa
    

class Pedido(models.Model):
    codigo_referencia = models.CharField(max_length=50, unique=True)
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    def __str__(self):
        return self.codigo_referencia  

# Hemos hecho una conexion n-m para producto pedido, es decir, varios pedidos pueden ser de varios productos y viceversa
class Producto_pedido(models.Model):
    producto_solicitado = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido_solicitado = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)

    


    

          
    