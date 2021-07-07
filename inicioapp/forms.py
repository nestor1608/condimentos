from django import forms
from django.forms import widgets

class ContactoForm (forms.Form):
    nombre=forms.CharField(label='Nombre',required=True)
    email=forms.CharField(label='Email',required=True)
    contenido=forms.CharField( label='Contenido', widget=forms.Textarea)