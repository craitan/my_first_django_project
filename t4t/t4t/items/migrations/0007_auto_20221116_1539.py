# Generated by Django 3.2.16 on 2022-11-16 13:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_alter_item_item_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_dexterity',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(150)]),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_intellect',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(150)]),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_strength',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(150)]),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_vitality',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(150)]),
        ),
    ]