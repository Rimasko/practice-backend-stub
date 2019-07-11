from django.contrib import admin

from apps.test.models import Test


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'random_string',
    )
    readonly_fields = (
        'random_string',
    )
