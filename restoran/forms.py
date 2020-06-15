from django import forms
from .models import Zakaz

class ZakazForm(forms.ModelForm):
    class Meta:
        model = Zakaz
        fields = ('name','email','date','number','table','foods')
