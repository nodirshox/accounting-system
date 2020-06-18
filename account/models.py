from django.db import models
from django.contrib.auth.models import User
# Models

class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(default='Product')
    image = models.ImageField(upload_to='products')
    price = models.IntegerField()
    def __str__(self):
        return self.name

class Package(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name

class Micropackage(models.Model):
    name = models.CharField(max_length=128)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Packagetype(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    micropackage = models.ForeignKey(Micropackage, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()

