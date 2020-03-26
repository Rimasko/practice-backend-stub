from django.contrib import admin
from apps.eats.models import Ingridient


@admin.register(Ingridient)
class IngridientAdmin(admin.ModelAdmin):
    list_display = ('name', 'cal')