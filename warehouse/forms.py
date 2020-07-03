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
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'min': 1}))
    class Meta: 
        model = Order
        fields = [
            'client',
            'product',
            'quantity'
        ]

class PaymentForm(forms.ModelForm):
    money = forms.IntegerField(widget=forms.NumberInput(attrs={'min': 1}))
    class Meta:
        model = Payment
        fields = [
            'order',
            'payment',
            'money'
        ]

class RecourceForm(forms.ModelForm):
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'min': 1}))
    class Meta:
        model = Recourse
        fields = [
            'product',
            'quantity'
        ]