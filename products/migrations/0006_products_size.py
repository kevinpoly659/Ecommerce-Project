# Generated by Django 4.1.3 on 2022-11-14 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_products_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='size',
            field=models.IntegerField(default=0),
        ),
    ]