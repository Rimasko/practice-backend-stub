from django.db import migrations, models
import json
import decimal

def load_data(apps, schema_editor):
    with open('/server/data.json', 'r') as file:
        data = json.load(file)
        Ingridient = apps.get_model('eats', 'Ingridient')
        for item in data:
            ing = Ingridient()
            ing.name = item['name']
            ing.cal =  decimal.Decimal(item['cal'])
            ing.save()


class Migration(migrations.Migration):

    dependencies = [
        ('eats', '0007_auto_20200325_1308'),
    ]

    operations = [
        migrations.RunPython(load_data),
    ]
