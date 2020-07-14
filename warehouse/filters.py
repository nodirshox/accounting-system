import django_filters
from django import forms
from django_filters import CharFilter
from .models import *

class ClientFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains', label="", widget=forms.TextInput(attrs={'autocomplete': 'off', 'class': 'form-control float-right', 'placeholder': 'Name'}))    
    number = CharFilter(field_name='number', lookup_expr='icontains', label='', widget=forms.TextInput(attrs={'autocomplete': 'off', 'class': 'form-control float-right', 'placeholder': 'Number'}))
    class Meta:
        model = Client
        fields = '__all__'
        exclude = ['warehouse', 'date']