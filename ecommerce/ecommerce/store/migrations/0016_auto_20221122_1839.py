# Generated by Django 3.2.16 on 2022-11-22 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_alter_product_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderItem',
            new_name='CartItem',
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
