# Generated by Django 4.1.3 on 2022-11-19 09:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_alter_products_added_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='added_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 19, 14, 38, 9, 319856)),
        ),
    ]
