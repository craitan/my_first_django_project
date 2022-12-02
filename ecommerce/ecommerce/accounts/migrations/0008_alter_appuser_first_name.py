# Generated by Django 3.2.16 on 2022-12-01 16:25

import django.core.validators
from django.db import migrations, models
import ecommerce.accounts.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_appuser_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=20, validators=[django.core.validators.MinLengthValidator(2), ecommerce.accounts.validators.validate_letters]),
        ),
    ]