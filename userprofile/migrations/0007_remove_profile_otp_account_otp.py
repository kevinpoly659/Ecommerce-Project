# Generated by Django 4.1.3 on 2022-11-15 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0006_profile_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='otp',
        ),
        migrations.AddField(
            model_name='account',
            name='otp',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]