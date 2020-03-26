from django.contrib import admin
from apps.eats.models import Dish


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'shop')