# Generated by Django 3.0.2 on 2020-02-04 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produkty', '0004_produktimage_is_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produktimage',
            name='image',
            field=models.ImageField(upload_to='products_images/'),
        ),
    ]
