# Generated by Django 5.1.6 on 2025-03-01 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booknow',
            name='Booking_reservation',
            field=models.DateField(),
        ),
    ]
