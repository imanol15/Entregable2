from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Pedido
from . import ProductoForm, PedidoForm
from django.views.generic import ListView, DetailView



class PedidoListView(ListView):
    model = Pedido



def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

def detalle_producto(request, referencia):
    producto = get_object_or_404(Producto, pk=referencia)
    return render(request, 'detalle_producto.html', {'producto': producto})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save()
            return redirect('detalle_producto', referencia=producto.referencia)
    else:
        form = ProductoForm()
    return render(request, 'crear_producto.html', {'form': form})

def editar_producto(request, referencia):
    producto = get_object_or_404(Producto, referencia=referencia)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save()
            return redirect('detalle_producto', referencia=producto.referencia)
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form, 'producto': producto})

def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'lista_pedidos.html', {'pedidos': pedidos})

def detalle_pedido(request, Pedido_codigo_referencia):
    pedido = get_object_or_404(Pedido, pk= Pedido_codigo_referencia)
    return render(request, 'detalle_pedido.html', {'pedido': pedido})

def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save()
            return redirect('detalle_pedido', codigo_referencia=pedido.codigo_referencia)
    else:
        form = PedidoForm()
    return render(request, 'crear_pedido.html', {'form': form})

