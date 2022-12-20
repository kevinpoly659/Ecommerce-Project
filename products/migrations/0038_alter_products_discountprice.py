# Generated by Django 4.1.3 on 2022-12-06 07:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0037_alter_products_discountprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='discountprice',
            field=models.IntegerField(default=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
        ),
    ]
