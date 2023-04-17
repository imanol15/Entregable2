from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Pedido,Componente
from django.views.generic import ListView, DetailView



class ProductoListView(ListView):
    model = Producto

class ProductoDetailView(DetailView):
    model = Producto

class PedidoListView(ListView):
    model = Pedido

class PedidoDetailView(DetailView):
    model = Pedido

class ComponenteListView(ListView):
    model = Componente

class ComponenteDetailView(DetailView):
    model = Componente

    



