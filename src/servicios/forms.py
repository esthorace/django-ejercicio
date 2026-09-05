from django import forms

from .models import Cliente, Servicio


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ("nombre", "telefono", "email")


class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ("nombre", "descripcion")
