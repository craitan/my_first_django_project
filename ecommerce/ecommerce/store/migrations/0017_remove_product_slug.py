# Generated by Django 3.2.16 on 2022-11-22 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_auto_20221122_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]