from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Warehouse(models.Model):
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    bonus = models.IntegerField(default=0, null=True)
    cash = models.IntegerField(default=0, null=True)
    terminal = models.IntegerField(default=0, null=True)
    balance = models.IntegerField(default=0, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.owner.first_name

class Client(models.Model):
    name = models.CharField(max_length=128, null=True)
    number = models.CharField(max_length=8, null=True)
    warehouse = models.ForeignKey(Warehouse, null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Recourse(models.Model):
    quantity = models.IntegerField()
    warehouse = models.ForeignKey(Warehouse, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.product.name + ', ' + str(self.quantity)
