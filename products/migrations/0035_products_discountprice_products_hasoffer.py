# Generated by Django 4.1.3 on 2022-12-05 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0034_alter_productoffer_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='discountprice',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='products',
            name='hasoffer',
            field=models.BooleanField(default=False),
        ),
    ]
