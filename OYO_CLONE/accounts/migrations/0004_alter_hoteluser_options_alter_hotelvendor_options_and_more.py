# Generated by Django 5.1.6 on 2025-02-27 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_hotelvendor_business_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hoteluser',
            options={},
        ),
        migrations.AlterModelOptions(
            name='hotelvendor',
            options={},
        ),
        migrations.AlterModelTable(
            name='hoteluser',
            table='hotel_user',
        ),
        migrations.AlterModelTable(
            name='hotelvendor',
            table='hotel_vendor',
        ),
    ]
