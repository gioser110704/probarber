from django.shortcuts import render
from .models import * #importa todos los modelos (tablas)
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponse
from django.db import IntegrityError
from .forms import *

# Create your views here.
def inicio (request):
    return render(request, 'inicio/inicio.html')

def menu_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/menu.html', {'Cliente': clientes})

def crear_clientes (request):
    formulario = clienteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request , "Cliente Creado correctamente")
        return redirect('menu_clientes')
    
    return render(request, 'clientes/crear.html', {'formulario': formulario})  

def editar_clientes (request, cedula):
    clientes = Cliente.objects.get(cedula=cedula)
    formulario = clienteFormEdit(request.POST or None, request.FILES or None, instance=clientes)
    if formulario.is_valid() and request.POST:
        formulario.save()
        messages.success(request , "Cliente Modificado correctamente")
        return redirect('menu_clientes')   
    return render(request, 'clientes/editar.html', {'formulario': formulario})

def eliminar_clientes (request, cedula):
    clientes = Cliente.objects.get(cedula=cedula)
    try:
        clientes.delete1()
        messages.success(request , "Cliente eliminado correctamente")
    except IntegrityError:
        messages.error(request, 'No se puede eliminar este cliente porque está referenciado en una factura.')
    return redirect('menu_clientes')


    