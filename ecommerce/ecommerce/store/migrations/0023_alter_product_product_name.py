# Generated by Django 3.2.16 on 2022-11-27 12:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_remove_cart_order_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=100, unique=True, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]
