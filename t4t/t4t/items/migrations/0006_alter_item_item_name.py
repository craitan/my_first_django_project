# Generated by Django 3.2.16 on 2022-11-15 18:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_auto_20221113_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_name',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]
