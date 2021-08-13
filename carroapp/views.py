from django.shortcuts import render

from .carro import Carro
from tiendaapp.models import Productos
from django.shortcuts import redirect


# Create your views here.
def Agregar_producto(request,producto_id):
    carro=Carro(request)
    producto=Productos.objects.get (id=producto_id)
    carro.add(producto=producto)
    return redirect("tienda")

def Eliminar_producto(request,producto_id):
    carro=Carro(request)
    producto=Productos.objects.get (id=producto_id)
    carro.remove(producto=producto)
    return redirect("tienda")

def Restar_producto(request,producto_id):
    carro=Carro(request)
    producto=Productos.objects.get (id=producto_id)
    carro.delete(producto=producto)
    return redirect("tienda")

def limpiar_carro(request):
    carro=Carro(request)
    carro.vaciar_carro
    return redirect("tienda")

# Create your views here.
