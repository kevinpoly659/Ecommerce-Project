# Generated by Django 4.1.3 on 2022-11-15 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_products_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='gender',
            field=models.CharField(max_length=200),
        ),
    ]