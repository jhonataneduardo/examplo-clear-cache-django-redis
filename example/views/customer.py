from rest_framework import viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from example.serializers import CustomerSeriaizer
from example.models.customer import Customer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSeriaizer

    @method_decorator(cache_page(60*2, key_prefix='cache_customer'))
    def dispatch(self, request, *args, **kwargs):
        return super(CustomerViewSet, self).dispatch(request, *args, **kwargs)
