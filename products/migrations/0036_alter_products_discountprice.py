# Generated by Django 4.1.3 on 2022-12-05 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0035_products_discountprice_products_hasoffer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='discountprice',
            field=models.IntegerField(default=0),
        ),
    ]
