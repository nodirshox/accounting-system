from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Warehouse(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    bonus = models.IntegerField(default=0, null=True)
    cash = models.IntegerField(default=0, null=True)
    terminal = models.IntegerField(default=0, null=True)
    active_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name

class Client(models.Model):
    name = models.CharField(max_length=128, null=True)
    number = models.CharField(max_length=8, null=True)
    warehouse = models.ForeignKey(Warehouse, null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Resource(models.Model):
    quantity = models.IntegerField(default=0, null=True)
    warehouse = models.ForeignKey(Warehouse, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.product.name + ', ' + str(self.quantity)
    

class Order(models.Model):
    client = models.ForeignKey(Client, null=True, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.client.name

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, null=True, on_delete=models.CASCADE)
    product = models.CharField(max_length=256)
    price = models.BigIntegerField(null=True)
    quantity = models.IntegerField(null=True)
    detail = models.TextField(blank=True)
    bonus = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product
    
class Payment(models.Model):
    order = models.ForeignKey(Order, null=True, on_delete=models.CASCADE)
    cash = models.IntegerField()
    plastic = models.IntegerField()
    bonus = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
