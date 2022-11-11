# Generated by Django 4.1.3 on 2022-11-09 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='men',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='men_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catagory', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('price_s', models.DecimalField(decimal_places=2, max_digits=5)),
                ('price_m', models.DecimalField(decimal_places=2, max_digits=5)),
                ('price_l', models.DecimalField(decimal_places=2, max_digits=5)),
                ('price_xl', models.DecimalField(decimal_places=2, max_digits=5)),
                ('picture', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='women',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='women_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catagory', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('price_s', models.DecimalField(decimal_places=2, max_digits=5)),
                ('price_m', models.DecimalField(decimal_places=2, max_digits=5)),
                ('price_l', models.DecimalField(decimal_places=2, max_digits=5)),
                ('price_xl', models.DecimalField(decimal_places=2, max_digits=5)),
                ('picture', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
