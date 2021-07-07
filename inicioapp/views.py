from django.http import request
from django.shortcuts import render
from .forms import ContactoForm

# Create your views here.

def inicio (request):
    return render (request,"inicioapp/index.html" )


def contacto(request):
    form= ContactoForm 
    return render (request,"inicioapp/contacto.html",{ 'formulario': form})