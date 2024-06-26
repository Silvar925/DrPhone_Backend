# Generated by Django 5.0.6 on 2024-06-02 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accessoriesoptions',
            options={'verbose_name': 'Варианты аксессуаров'},
        ),
        migrations.AlterModelOptions(
            name='imacoptions',
            options={'verbose_name': 'Вариант IMac', 'verbose_name_plural': "Варианты IMac'ов"},
        ),
        migrations.AlterModelOptions(
            name='phonesoptions',
            options={'verbose_name': 'Варианты телефона'},
        ),
        migrations.AddField(
            model_name='accessoriesoptions',
            name='used',
            field=models.BooleanField(default=False, verbose_name='Подержанный'),
        ),
        migrations.AddField(
            model_name='imacoptions',
            name='used',
            field=models.BooleanField(default=False, verbose_name='Подержанный'),
        ),
    ]
