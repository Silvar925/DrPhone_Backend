# Generated by Django 5.0.7 on 2024-07-22 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0013_rename_accessories_accessoriesoptions_device_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessoriesoptions',
            name='unique_id',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='Уникальный ID'),
        ),
    ]
