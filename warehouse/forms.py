from django import forms
from . models import *

class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = []


class ClientForm(forms.ModelForm):
    name = forms.CharField(label='Full name', widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    number = forms.CharField(label='Client Code', widget=forms.TextInput(attrs={'placeholder': 'UZ123456', 'autocomplete': 'off', 'minlength': 8, 'maxlength': 8, 'oninput': 'this.value = this.value.toUpperCase()'}))
    class Meta:
        model = Client
        fields = [
            'name',
            'number'
        ]

class OrderForm(forms.ModelForm):
    class Meta: 
        model = Order
        fields = '__all__'

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'

class RecourceForm(forms.ModelForm):
    class Meta:
        model = Recourse
        fields = '__all__'