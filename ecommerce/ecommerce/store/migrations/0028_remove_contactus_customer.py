# Generated by Django 3.2.16 on 2022-12-02 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0027_contactus_massage_checked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='customer',
        ),
    ]
