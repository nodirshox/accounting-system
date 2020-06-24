from django.forms import ModelForm
from . models import *

class WarehouseForm(ModelForm):
    class Meta:
        model = Warehouse
        fields = '__all__'

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class OrderForm(ModelForm):
    class Meta: 
        model = Order
        fields = '__all__'