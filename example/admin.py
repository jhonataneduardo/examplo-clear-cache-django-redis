from django.contrib import admin
from example.models.product import Product
from example.models.customer import Customer

admin.site.register(Product)
admin.site.register(Customer)
