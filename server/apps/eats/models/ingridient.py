from django.db import models


class Ingridient(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100)
    cal = models.DecimalField(decimal_places=2, max_digits=10, default=0)

    class Meta:
        verbose_name = "Ингридиент"
        verbose_name_plural = "Ингридиенты"

    def __str__(self):
        return self.name