from django.shortcuts import render
from .models import * #importa todos los modelos (tablas)
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponse
from django.db import IntegrityError
from .forms import *
from django.db import connection

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
        messages.error(request, 'No se puede eliminar este cliente porque está referenciado en una cita.')
    return redirect('menu_clientes')

def servicio(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios/menu.html', {'Servicio': servicios})

    
def crear_servicio (request):
    formulario = servicioForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request , "Cliente Creado correctamente")
        return redirect('servicios')
    
    return render(request, 'servicios/crear.html', {'formulario': formulario}) 

def editar_servicio (request,id):
    servicios = Servicio.objects.get(id=id)
    formulario = servicioFormEdit(request.POST or None, request.FILES or None, instance=servicios)
    if formulario.is_valid() and request.POST:
        formulario.save()
        messages.success(request , "Servicio Modificado correctamente")
        return redirect('servicios')   
    return render(request, 'servicios/editar.html', {'formulario': formulario})

def eliminar_servicio (request,id):
    servicios = Servicio.objects.get(id=id)
    try:
        servicios.delete1()
        messages.success(request , "Servicio eliminado correctamente")
    except IntegrityError:
        messages.error(request, 'No se puede eliminar este servicio.')
    return redirect('servicios') 




def barbero(request):
    barberos = Barbero.objects.all()
    return render(request, 'barberos/menu.html', {'Barbero': barberos})

def crear_barberos (request):
    formulario = barberoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request , "Barbero Creado correctamente")
        return redirect('barberos')
    
    return render(request, 'barberos/crear.html', {'formulario': formulario})  

def editar_barberos  (request, id):
    barberos  = Barbero.objects.get(id=id)
    formulario = barberoFormEdit(request.POST or None, request.FILES or None, instance=barberos)
    if formulario.is_valid() and request.POST:
        formulario.save()
        messages.success(request , "Barbero Modificado correctamente")
        return redirect('barberos')   
    return render(request, 'barberos/editar.html', {'formulario': formulario})

def eliminar_barberos  (request, id):
    barberos  = Barbero.objects.get(id = id)
    try:
        barberos.delete1()
        messages.success(request , "Barbero eliminado correctamente")
    except IntegrityError:
        messages.error(request, 'No se puede eliminar este barbero porque está referenciado en una cita')
    return redirect('barberos')


def cita (request):
    with connection.cursor() as cursor:
        cursor.execute("""
            select cc.id, c.cedula, c.nombre , b.nombre, cc.fecha, cc.hora, s.nombre, duracion, precio from cliente c 
            inner join cita cc on c.cedula = cc.cliente_id
            inner join barbero b on cc.barbero_id = b.id
            inner join servicio s on cc.servicio_id = s.id;

        """)
        citas = cursor.fetchall()
        return render(request, 'citas/menu.html', {'cita': citas})
    
def crear_citas (request):
    formulario = citaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request , "Cita registrada")
        return redirect('citas')
    
    return render(request, 'citas/crear.html', {'formulario': formulario})  

def editar_citas (request, id):
    citas  = Cita.objects.get(id=id)
    formulario = citaFormEdit(request.POST or None, request.FILES or None, instance=citas)
    if formulario.is_valid() and request.POST:
        formulario.save()
        messages.success(request , "Cita Modificada correctamente")
        return redirect('citas')   
    return render(request, 'citas/editar.html', {'formulario': formulario})

def eliminar_citas (request, id):
    citas  = Cita.objects.get(id = id)
    try:
        citas.delete1()
        messages.success(request , "Cita eliminado correctamente")
    except IntegrityError:
        messages.error(request, 'No se puede eliminar esta cita')
    return redirect('citas')


def especialidad(request):
    especialidads = Especialidad.objects.all()
    return render(request, 'especialidads/menu.html', {'Especialidad': especialidads})

def crear_especialidad (request):
    formulario = especialidadForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request , "Especialidad Creada correctamente")
        return redirect('especialidad')
    
    return render(request, 'especialidads/crear.html', {'formulario': formulario})  

def editar_especialidad (request, id):
    especialidads = Especialidad.objects.get(id=id)
    formulario = especialidadFormEdit(request.POST or None, request.FILES or None, instance=especialidads)
    if formulario.is_valid() and request.POST:
        formulario.save()
        messages.success(request , "Especialidad Modificado correctamente")
        return redirect('especialidad')   
    return render(request, 'especialidads/editar.html', {'formulario': formulario})

def eliminar_especialidad (request, id):
    especialidads = Especialidad.objects.get(id=id)
    try:
        especialidads.delete1()
        messages.success(request , "especialidad eliminada correctamente")
    except IntegrityError:
        messages.error(request, 'No se puede eliminar esta especialidad')
    return redirect('especialidad')

from django.db import connection
from django.shortcuts import render

###REPORTES### ###REPORTES### ###REPORTES### ###REPORTES### ###REPORTES### ###REPORTES### ###REPORTES### ###REPORTES### ###
 
def servicios_mas_vendidos(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT s.nombre AS servicio, COUNT(c.servicio_id) AS cantidad_vendida, SUM(s.precio) AS ingreso_total, s.precio
            FROM cita c
            JOIN servicio s ON c.servicio_id = s.id
            GROUP BY s.nombre, s.precio
            ORDER BY cantidad_vendida DESC;
        """)
        servicios = cursor.fetchall()
    return render(request, 'reportes/masvendido.html', {'servicios': servicios})
    
def clientes_que_mas_compran(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT cl.nombre, cl.apellido, COUNT(c.id) AS citas_realizadas, SUM(s.precio) AS total_gastado
            FROM cita c
            JOIN cliente cl ON c.cliente_id = cl.cedula
            JOIN servicio s ON c.servicio_id = s.id
            GROUP BY cl.nombre, cl.apellido
            ORDER BY total_gastado DESC;
        """)
        clientes = cursor.fetchall()
    return render(request, 'reportes/clientes_que_mas_compran.html', {'clientes': clientes})

#para cambiar el mes cambiar el numero  WHERE MONTH(c.fecha) = 
def citas_por_mes(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT c.id, cl.cedula, cl.nombre, cl.apellido, c.fecha, c.hora, s.nombre AS servicio, s.precio
            FROM cita c
            JOIN cliente cl ON c.cliente_id = cl.cedula
            JOIN servicio s ON c.servicio_id = s.id
            WHERE MONTH(c.fecha) = 7
            ORDER BY c.fecha, c.hora;
        """)
        citas = cursor.fetchall()
    return render(request, 'reportes/citas_por_mes.html', {'citas': citas})

def barberos_mas_solicitados(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT b.nombre, b.apellido, COUNT(c.id) AS servicios_realizados
            FROM cita c
            JOIN barbero b ON c.barbero_id = b.id
            GROUP BY b.nombre, b.apellido
            ORDER BY servicios_realizados DESC;
        """)
        barberos = cursor.fetchall()
    return render(request, 'reportes/barberos_mas_solicitados.html', {'barberos': barberos})