# Create your models here.
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    description = models.TextField()
    photo = models.ImageField(upload_to='uploads/', null=True)
    cat_id = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='uploads/', null=True)
    address = models.CharField(max_length=30)
    contact = models.IntegerField(null=True)

    def __str__(self):
        return self.user.first_name


class CartItem(models.Model):
    cus_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    food_id = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __int__(self):
        return self.id


class Order(models.Model):
    cus_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    food_id = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date_order = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.id
