# Generated by Django 4.1.3 on 2022-11-24 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='size',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
