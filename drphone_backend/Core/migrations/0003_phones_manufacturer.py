# Generated by Django 5.0.6 on 2024-06-02 13:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BaseSettings', '0002_manufacturer'),
        ('Core', '0002_alter_accessoriesoptions_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='phones',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='BaseSettings.manufacturer', verbose_name='Производитель'),
        ),
    ]
