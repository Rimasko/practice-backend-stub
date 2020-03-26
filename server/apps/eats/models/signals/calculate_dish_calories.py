from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from apps.eats.models import Dish, Ingridient


@receiver(post_save, sender=Dish)
def calculate_dish_calories(sender, instance, **kwargs):
    summary_cal = 0
    for ingridient in instance.ingridients.all():
        summary_cal += ingridient.cal
    instance.summary_cal = summary_cal





