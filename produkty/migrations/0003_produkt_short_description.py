# Generated by Django 3.0.2 on 2020-02-02 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produkty', '0002_produkt_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='produkt',
            name='short_description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
