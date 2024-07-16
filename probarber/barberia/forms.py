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

   