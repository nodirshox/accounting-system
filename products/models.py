from django.db import models

# Model for Product, Package

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

class Packagesize(models.Model):
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    micropackage = models.ForeignKey(Micropackage, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Packageprice(models.Model):
    
    price = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)