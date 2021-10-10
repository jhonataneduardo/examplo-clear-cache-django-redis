from rest_framework import viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from example.serializers import ProductSeriaizer
from example.models.product import Product


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSeriaizer

    @method_decorator(cache_page(60*2, key_prefix='cache_product'))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductViewSet, self).dispatch(request, *args, **kwargs)
