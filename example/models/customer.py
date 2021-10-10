from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache


class Customer(models.Model):

    first_name = models.CharField(verbose_name="First Name", max_length=80)
    last_name = models.CharField(verbose_name="Last Name", max_length=80)

    def __str__(self):
        return self.first_name


@receiver(post_save, sender=Customer)
def update_customer(sender, instance, **kwargs):
    customer_caches_list = cache.keys("*.cache_customer.*")
    for key_cache in customer_caches_list:
        cache.delete_pattern(key_cache)


@receiver(post_delete, sender=Customer)
def delete_customer(sender, instance, **kwargs):
    customer_caches_list = cache.keys("*.cache_customer.*")
    for key_cache in customer_caches_list:
        cache.delete_pattern(key_cache)
