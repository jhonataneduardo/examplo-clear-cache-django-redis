from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache


class Product(models.Model):

    name = models.CharField(verbose_name="Name", max_length=80)
    price = models.FloatField(verbose_name="Price", max_length=4)
    description = models.TextField(verbose_name="Description")

    def __str__(self):
        return self.name


@receiver(post_save, sender=Product)
def update_product(sender, instance, **kwargs):
    product_caches_list = cache.keys("*.cache_product.*")
    for key_cache in product_caches_list:
        cache.delete_pattern(key_cache)


@receiver(post_delete, sender=Product)
def delete_product(sender, instance, created, **kwargs):
    product_caches_list = cache.keys("*.cache_product.*")
    for key_cache in product_caches_list:
        cache.delete_pattern(key_cache)
