# Generated by Django 4.1.3 on 2022-11-14 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_products_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='gender',
            field=models.TextField(default='MALE', max_length=200, unique=True),
        ),
    ]