from django.db import models
from apps.eats.models import Ingridient, Shop


class Dish(models.Model):
    name = models.CharField(verbose_name="Название", max_length=100)
    photo = models.ImageField(verbose_name="Изображение", upload_to='photo/dish')
    summary_cal = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    ingridients = models.ManyToManyField(Ingridient,
                                         related_name='dishes',
                                         verbose_name="Ингридиенты",
                                         blank=True)
    shop = models.ForeignKey(Shop,
                             on_delete=models.CASCADE,
                             related_name='dishes',
                             verbose_name='Заведение')

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"

    def __str__(self):
        return self.name
