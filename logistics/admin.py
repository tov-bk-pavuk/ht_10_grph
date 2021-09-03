from django.contrib import admin

from .models import City, Client, Product, Supplier

admin.site.register(City)
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Supplier)
