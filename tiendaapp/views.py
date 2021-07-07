from django.shortcuts import render
from .models import CateProducto,Productos

# Create your views here.
def tienda (request):
    productos=Productos.objects.all()
    categoria = CateProducto.objects.all()
    #carro = Carro(request)
    
    return render(request,'tiendaapp/tienda.html', {'productos':productos})