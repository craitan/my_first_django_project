# Generated by Django 3.2.16 on 2022-12-01 16:57

import django.core.validators
from django.db import migrations, models
import ecommerce.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0024_auto_20221201_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='first_name',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2), ecommerce.core.validators.validate_letters]),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='last_name',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2), ecommerce.core.validators.validate_letters]),
        ),
    ]
