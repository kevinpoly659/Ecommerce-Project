# Generated by Django 4.1.3 on 2022-11-14 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catagory', '0002_remove_catagories_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='catagories',
            name='gender',
            field=models.CharField(default=True, max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
