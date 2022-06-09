from dataclasses import fields
from tkinter.tix import Form
from xml.parsers.expat import model
from django import forms
from .models import Contato, Pessoa

class PessoaForm(forms.ModelForm):
    data_nascimento = forms.DateField(
        widget=forms.TextInput(
            attrs={"type": "date"}
        )
    )

    class Meta:
        model = Pessoa   
        fields = ['nome_completo','data_nascimento','ativa']


class ContatoForm(forms.ModelForm):
   
    class Meta:
        model = Contato
        fields = ['nome','email','telefone']