# Generated by Django 5.0.7 on 2024-07-22 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0012_accessoriesoptions_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accessoriesoptions',
            old_name='accessories',
            new_name='device',
        ),
        migrations.RenameField(
            model_name='imacoptions',
            old_name='imac',
            new_name='device',
        ),
        migrations.RenameField(
            model_name='phonesoptions',
            old_name='phone',
            new_name='device',
        ),
    ]
