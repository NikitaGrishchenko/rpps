# Generated by Django 3.0.8 on 2020-07-09 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questioning', '0007_auto_20200707_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='questionnaire/', verbose_name='Файл анкеты'),
        ),
    ]