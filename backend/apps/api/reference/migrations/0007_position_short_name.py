# Generated by Django 3.0.8 on 2020-07-04 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0006_auto_20200704_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='short_name',
            field=models.CharField(blank=True, max_length=31, null=True, verbose_name='Краткое наименование'),
        ),
    ]
