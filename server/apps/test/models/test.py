from django.db import models


class Test(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Название',
    )
    random_string = models.CharField(
        max_length=255,
        verbose_name='Рандномная строка',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тест'
