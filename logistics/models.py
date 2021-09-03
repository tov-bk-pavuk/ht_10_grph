from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    city_name = models.CharField(max_length=20, verbose_name='Город')

    def __str__(self):
        return self.city_name


class Supplier(models.Model):
    name = models.CharField(max_length=20, verbose_name='Поставщик')
    legal_form = models.CharField(choices=[
        ('TOV', 'TOV'),
        ('FOP', 'FOP'),
        ('PAT', 'PAT')],
        max_length=20, verbose_name='Орг.форма')
    city = models.OneToOneField(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(unique=True, max_length=250)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    availability = models.PositiveIntegerField(verbose_name='Наличие')
    supplier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING, default=1)

    def __str__(self):
        return self.name


class Client(models.Model):
    first_name = models.CharField(max_length=20, verbose_name='Имя Клиента', default='Client')
    last_name = models.CharField(max_length=20, verbose_name='Фамилия Клиента')
    phone = models.CharField(max_length=10, unique=True)
    product = models.ManyToManyField(Product)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name
