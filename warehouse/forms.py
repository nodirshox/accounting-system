from django import forms
from . models import *

class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = [
            'user',
            'bonus',
            'cash',
            'terminal'
        ]
        widgets = {
            'user': forms.TextInput(attrs={'hidden': True})
        }

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta: 
        model = Order
        fields = '__all__'