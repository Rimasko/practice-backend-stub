from django.db import models
from django.contrib.auth.models import User


class Shop(models.Model):
    Owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              verbose_name="Владелец",
                              related_name="shops")
    name = models.CharField(verbose_name="Название заведения", max_length=100)
    photo = models.ImageField(verbose_name="Фоторгафия заведения", upload_to="photo/eats")
    work_start = models.TimeField(verbose_name="Начало рабочего дня", auto_now=False)
    work_end = models.TimeField(verbose_name='Конец рабочего дня', auto_now=False)
    addres = models.CharField(verbose_name="Адрес заведения", max_length=200)
    averge_cost = models.FloatField(verbose_name="Средняя стоимость", default=0)
    lat = models.DecimalField(verbose_name="lat", max_digits=10, decimal_places=5, default=0.0)
    lon = models.DecimalField(verbose_name="lon", max_digits=10, decimal_places=5, default=0.0)

    class Meta:
        verbose_name = "Заведение"
        verbose_name_plural = "Заведенияфц"

    def __str__(self):
        return self.name
