from django.db.models import fields
from rest_framework import serializers
from example.models.product import Product
from example.models.customer import Customer


class ProductSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description']


class CustomerSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name']
