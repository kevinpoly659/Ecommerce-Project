# Generated by Django 4.1.3 on 2022-11-15 06:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_products_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='added_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 15, 12, 26, 46, 309950)),
        ),
    ]
