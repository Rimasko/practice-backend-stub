# Generated by Django 2.2.1 on 2019-07-08 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='random_string',
            field=models.CharField(default='asd', max_length=255, verbose_name='Рандномная строка'),
            preserve_default=False,
        ),
    ]
