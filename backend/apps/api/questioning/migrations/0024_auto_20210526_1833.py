# Generated by Django 3.1 on 2021-05-26 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questioning', '0023_auto_20210427_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoryquestionnaireuser',
            name='use_internet_resource_link',
            field=models.BooleanField(default=False, verbose_name='Добавить поле для Интернет-ресурса?'),
        ),
        migrations.AddField(
            model_name='filecategoryquestionnaireuser',
            name='internet_resource_link',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на Интернет-ресурс'),
        ),
    ]
