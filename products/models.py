from django.db import models

# Model for Product, Package

class Product(models.Model):
    name = models.CharField(max_length=128, null=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='products', null=True)
    product_price = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Package(models.Model):  
    name = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.name

class Pack(models.Model):
    name = models.CharField(max_length=128, null=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Quantity(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    pack = models.ForeignKey(Pack, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)

    def __str__(self):
        return self.pack.name + ', ' + self.product.name

class Price(models.Model):
    price = models.IntegerField(null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)

    def __str__(self):
        return self.package.name + ' - ' + self.product.name
