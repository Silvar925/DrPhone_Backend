# Generated by Django 5.0.7 on 2024-07-22 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BaseSettings', '0003_alter_manufacturer_options'),
        ('Core', '0011_remove_accessories_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessoriesoptions',
            name='images',
            field=models.ManyToManyField(to='BaseSettings.imagesproduct', verbose_name='Изображение'),
        ),
    ]
