# Generated by Django 3.0.2 on 2020-01-31 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zakazy', '0002_auto_20200131_1251'),
    ]

    operations = [
        migrations.RenameField(
            model_name='zakaz',
            old_name='total_amount',
            new_name='total_price',
        ),
    ]
