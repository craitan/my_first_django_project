# Generated by Django 3.2.16 on 2022-11-18 11:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_shippingaddress_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
