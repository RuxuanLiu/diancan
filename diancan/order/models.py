from django.db import models

# Create your models here.


class User(models.Model):
    openid = models.CharField(max_length=500)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.openid


class Seller(models.Model):
    name = models.CharField(max_length=100)
    rank = models.IntegerField(max_length=1)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(max_length=10)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    time = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.time
