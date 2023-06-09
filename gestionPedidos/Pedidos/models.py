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

# Clase Categiria
class Categoria(models.Model):
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.categoria
          
# Clase producto
class Producto(models.Model):
    referencia = models.CharField(max_length=50, unique=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    componentes = models.ManyToManyField(Componente)

    def __str__(self):
        return f"{self.referencia}" 

#Clase cliente    
class Cliente(models.Model):
    cif = models.CharField(max_length=50)
    nombre_empresa = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    datos_contacto = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre_empresa
    

#Clase pedido
class Pedido(models.Model):
    codigo_referencia = models.CharField(max_length=50, unique=True)
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    preciototal = models.DecimalField(max_digits=10, decimal_places=2)
    producto = models.ManyToManyField(Producto, through="ProductoPedido")
    
    def __str__(self):
        return self.codigo_referencia 


# Hemos hecho una conexion n-m para producto pedido, es decir, varios pedidos pueden ser de varios productos y viceversa
class ProductoPedido(models.Model):
    producto_solicitado = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido_solicitado = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    def __str__(self):
        return f"{self.producto_solicitado} - {self.pedido_solicitado} - {self.cantidad} " 

class ProductoComponente(models.Model):
    producto_solicitado = models.ForeignKey(Producto, on_delete=models.CASCADE)
    componente_solicitado = models.ForeignKey(Componente, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.producto_solicitado} - {self.componente_solicitado} "
    