from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.eats.models import Dish, Shop


@receiver(post_save, sender=Dish)
def calculate_cost(sender, instance, **kwargs):
    shop = Shop.objects.get(pk=instance.shop_id)
    dish_count = shop.dishes.count()
    dish_sum = 0
    for dish in shop.dishes.all():
        dish_sum += dish.cost
    dish_sum /= dish_count
    shop.averge_cost = dish_sum
    shop.save()
