# Generated by Django 5.0.6 on 2024-07-09 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0004_alter_accessoriesoptions_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='phonesoptions',
            options={'verbose_name': 'Вариант телефона', 'verbose_name_plural': 'Варианты телефонаов'},
        ),
        migrations.AddField(
            model_name='phonesoptions',
            name='count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Штук в наличии'),
        ),
    ]
