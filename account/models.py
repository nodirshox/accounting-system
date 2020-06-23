from django.db import models

class Currency(models.Model):
    rate = models.IntegerField(default=0, null=True)
    
    def __str__(self):
        return str(self.rate)

class Subscription(models.Model):
    fee = models.IntegerField(default=0, null=True)

    def __str__(self):
        return str(self.fee)
