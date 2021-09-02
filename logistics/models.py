from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    city_name = models.CharField(max_length=20, verbose_name='Город')

    def __str__(self):
        return self.city_name


class Supplier(models.Model):
    name = models.CharField(max_length=20, verbose_name='Поставщик')
    legal_form = models.CharField(choices=['TOV', 'FOP', 'PAT'],
                                  max_length=20, verbose_name='Орг.форма')
    city = models.OneToOneField(City.city_name, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(unique=True, max_length=250)
    price = models.DecimalField(max_digits=8, decimal_places=2, min_value=0)
    availability = models.PositiveIntegerField

    def __str__(self):
        return self.name, self.availability


class Client(User):
    first_name = User.first_name
    last_name = User.last_name
    phone = models.CharField(max_length=10, unique=True)
    product = models.ManyToManyField(Product.name)
    city = models.ForeignKey(City.city_name, on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name, self.first_name, self.city, self.phone
