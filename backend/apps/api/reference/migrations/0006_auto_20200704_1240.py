# Generated by Django 3.0.8 on 2020-07-04 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0005_auto_20200704_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='department',
            name='short_name',
            field=models.CharField(blank=True, max_length=31, null=True, unique=True, verbose_name='Краткое наименование'),
        ),
    ]
