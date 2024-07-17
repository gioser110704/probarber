from django import forms
from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.forms import Form, ModelForm
from django.forms import Select, DateInput, TextInput, CharField
from django import forms

class clienteForm(forms.ModelForm):
    cedula = forms.IntegerField(label = "Cedula del Cliente", widget= forms.NumberInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese la cedula',
            'id': 'cedula',
            'required' : 'required',  }))  
    
    nombre = forms.CharField(label = "Nombre del Cliente", widget= forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese el nombre del Cliente',
            'id': 'nombre',
            'required' : 'required',  } ))         
    
    apellido = forms.CharField(label = "Apellido del cliente", widget= forms.TextInput(
        attrs = { 'class': 'form-control',
                 'placeholder': 'Ingrese el apellido del cliente',
                 'id': 'descripcion',
                 'required' : 'required', }  ))                 
    
    telefono= forms.IntegerField(label = "Numero de telefono", widget= forms.NumberInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese el numero de telefono',
            'id': 'telefono',
            'required' : 'required', } )) 
    
    direccion = forms.CharField(label = "Direccion del Cliente", widget= forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese la direccion del cliente',
            'id': 'direccion',
            'required' : 'required',  }))  
    
    correo = forms.CharField(label = "Correo del Cliente", widget= forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese el correo del cliente',
            'id': 'correo',
            'required' : 'required',  })) 
    
    class Meta:
        model = Cliente
        fields = '__all__'
        
class clienteFormEdit(forms.ModelForm):
        
    nombre = forms.CharField(label = "Nombre del Cliente", widget= forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese el nombre del Cliente',
            'id': 'nombre',
            'required' : 'required',  } ))         
    
    apellido = forms.CharField(label = "Apellido del cliente", widget= forms.TextInput(
        attrs = { 'class': 'form-control',
                 'placeholder': 'Ingrese el apellido del cliente',
                 'id': 'descripcion',
                 'required' : 'required', }  ))                 
    
    telefono= forms.IntegerField(label = "Numero de telefono", widget= forms.NumberInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese el numero de telefono',
            'id': 'telefono',
            'required' : 'required', } )) 
    
    direccion = forms.CharField(label = "Direccion del Cliente", widget= forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese la direccion del cliente',
            'id': 'direccion',
            'required' : 'required',  }))  
    
    correo = forms.CharField(label = "Correo del Cliente", widget= forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese el correo del cliente',
            'id': 'correo',
            'required' : 'required',  })) 
    
    class Meta:
        model = Cliente
        fields = fields = ['nombre', 'apellido', 'telefono', 'direccion', 'correo']


class servicioForm(forms.ModelForm): 
    
    nombre = forms.CharField(label = "Nombre del Servicio", widget= forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese el Nombre del Servicio"',
            'id': 'duracion',
            'required' : 'required',  } ))   
    
    duracion = forms.CharField(label = "Duracion del Servicio", widget= forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese la Duracion del Servicio',
            'id': 'duracion',
            'required' : 'required',  } ))   
    
    
    class Meta:
        model = Servicio
        fields = '__all__'
        widgets = {
            'precio': TextInput(attrs={
                'readonly': False,
                'class': 'form-control',
            })
        }
        
class servicioFormEdit(forms.ModelForm): 
    
    nombre = forms.CharField(label = "Nombre del Servicio", widget= forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese el Nombre del Servicio',
            'id': 'duracion',
            'required' : 'required',  } ))   
    
    duracion = forms.CharField(label = "Duracion del Servicio", widget= forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese la Duracion del Servicio',
            'id': 'duracion',
            'required' : 'required',  } ))   
    
    
    class Meta:
        model = Servicio
        fields = ['nombre', 'duracion', 'precio']
        widgets = {
            'precio': TextInput(attrs={
                'readonly': False,
                'class': 'form-control',
            })
        }
        


class barberoForm(forms.ModelForm):
    nombre = forms.CharField(label = "Nombre del Barbero", widget= forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese el nombre del Barbero',
            'id': 'nombre',
            'required' : 'required',  } ))         
    
    apellido = forms.CharField(label = "Apellido del Barbero", widget= forms.TextInput(
        attrs = { 'class': 'form-control',
                 'placeholder': 'Ingrese el apellido del Barbero',
                 'id': 'descripcion',
                 'required' : 'required', }  ))   
    

    
    class Meta:
        model = Barbero   #NOMBRE DE LA TABLA
        fields = '__all__'
        widgets = {
        'id_especialidad': forms.Select(  attrs = {
            'class': 'form-control',
            'placeholder': 'Categoria del zapato',
            'id': 'categoria',
            'required' : 'required',})}
        
        
class barberoFormEdit(forms.ModelForm):
    nombre = forms.CharField(label = "Nombre del Barbero", widget= forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese el nombre del Barbero',
            'id': 'nombre',
            'required' : 'required',  } ))         
    
    apellido = forms.CharField(label = "Apellido del Barbero,", widget= forms.TextInput(
        attrs = { 'class': 'form-control',
                 'placeholder': 'Ingrese el apellido del Barbero',
                 'id': 'descripcion',
                 'required' : 'required', }  ))   
    

    
    class Meta:
        model = Barbero   #NOMBRE DE LA TABLA
        fields = '__all__'
        widgets = {
        'id_especialidad': forms.Select(  attrs = {
            'class': 'form-control',
            'placeholder': 'especialidad del barbero',
            'id': 'categoria',
            'required' : 'required',})}
        
        
        
        
class citaForm (forms.ModelForm):
    fecha = forms.DateField(label = "Fecha de la cita", widget= forms.DateInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese la fecha de la cita',
            'id': 'nombre',
            'required' : 'required',  } ))         
    
    hora = forms.CharField(label = "Hora de la cita", widget= forms.TextInput(
        attrs = { 'class': 'form-control',
                 'placeholder': 'Ingrese la hora de la cita',
                 'id': 'descripcion',
                 'required' : 'required', }  ))   
    

    
    class Meta:
        model = Cita  #NOMBRE DE LA TABLA
        fields = '__all__'
        widgets = {
        'cliente_id': forms.Select(  attrs = {
            'class': 'form-control',
            'placeholder': 'especialidad del barbero',
            'id': 'categoria',
            'required' : 'required',}),
        
        'barbero_id': forms.Select(  attrs = {
            'class': 'form-control',
            'placeholder': 'especialidad del barbero',
            'id': 'categoria',
            'required' : 'required',}),
        
        'servicio_id': forms.Select(  attrs = {
            'class': 'form-control',
            'placeholder': 'especialidad del barbero',
            'id': 'categoria',
            'required' : 'required',}),
        
        },

class citaFormEdit(forms.ModelForm):
    fecha = forms.DateField(label = "Fecha de la cita", widget= forms.DateInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese la fecha de la cita',
            'id': 'nombre',
            'required' : 'required',  } ))         
    
    hora = forms.CharField(label = "Hora de la cita", widget= forms.TextInput(
        attrs = { 'class': 'form-control',
                 'placeholder': 'Ingrese la hora de la cita',
                 'id': 'descripcion',
                 'required' : 'required', }  ))   
    

    
    class Meta:
        model = Cita  #NOMBRE DE LA TABLA
        fields = '__all__'
        widgets = {
        'cliente_id': forms.Select(  attrs = {
            'class': 'form-control',
            'placeholder': 'especialidad del barbero',
            'id': 'categoria',
            'required' : 'required',}),
        
        'barbero_id': forms.Select(  attrs = {
            'class': 'form-control',
            'placeholder': 'especialidad del barbero',
            'id': 'categoria',
            'required' : 'required',}),
        
        'servicio_id': forms.Select(  attrs = {
            'class': 'form-control',
            'placeholder': 'especialidad del barbero',
            'id': 'categoria',
            'required' : 'required',}),
        
        },


class especialidadForm(forms.ModelForm): 
    
    descripcion = forms.CharField(label = "Especialidad", widget= forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Nombre de la especialidad',
            'id': 'especialidad',
            'required' : 'required',  } ))   
    
    
    class Meta:
        model = Especialidad
        fields = '__all__'
        
class especialidadFormEdit(forms.ModelForm): 
    
    descripcion = forms.CharField(label = "Especialidad", widget= forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Nombre de la especialidad',
            'id': 'especialidad',
            'required' : 'required',  } ))   
    
    
    class Meta:
        model = Especialidad
        fields = '__all__'