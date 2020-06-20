from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Client
class Client(models.Model):
    name = models.CharField(max_length=128, null=True)
    number = models.CharField(max_length=8, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Warehouse
class Warehouse(models.Model):
    bonus = models.IntegerField(default=0, null=True)
    cash = models.IntegerField(default=0, null=True)
    bankaccount = models.IntegerField(default=0, null=True)
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    active = models.BooleanField(default=True)

class Recourse(models.Model):
    quantity = models.IntegerField()
    warehouse = models.ForeignKey(Warehouse, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
