# Generated by Django 3.1 on 2021-06-03 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questioning', '0025_auto_20210526_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoryquestionnaire',
            name='max_weight',
            field=models.FloatField(blank=True, null=True, verbose_name='Максимальная возможная весомость показателя'),
        ),
    ]