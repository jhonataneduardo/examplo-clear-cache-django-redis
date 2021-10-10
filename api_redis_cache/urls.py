from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from example.views.product import ProductViewSet
from example.views.customer import CustomerViewSet

router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('customers', CustomerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
