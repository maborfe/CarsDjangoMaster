# Generated by Django 4.2.7 on 2023-12-04 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Car', '0002_car_photo_alter_car_factoryyear_alter_car_modelyear_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='value',
            new_name='price',
        ),
    ]
