from django import forms
from .models import *

class studentForm(forms.ModelForm):
    class Meta:
        model =register
        fields='__all__'
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'mail':forms.TextInput(attrs={'class':'form-control'})

        }