from django.db import models

# Model for Product, Package

class Product(models.Model):
    name = models.CharField(max_length=128, null=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='products', null=True)
    price = models.IntegerField(null=True)
    def __str__(self):
        return self.name

class Package(models.Model):  
    name = models.CharField(max_length=128, null=True)
    def __str__(self):
        return self.name

class Micropackage(models.Model):
    name = models.CharField(max_length=128, null=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Packagesize(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    micropackage = models.ForeignKey(Micropackage, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)

class Packageprice(models.Model):
    price = models.IntegerField(null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)

class Currency(models.Model):
    # 1 point in sum: e.x: 1 point = 10 000 sum
    money = models.IntegerField(null=True)
