# Generated by Django 3.1 on 2021-12-16 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_api', '0010_auto_20200914_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfile',
            name='type_file',
            field=models.IntegerField(choices=[(22, 'Благодарность'), (13, 'Выходные данные'), (20, 'Грамота'), (18, 'Грант'), (16, 'Диплом'), (0, 'Другое'), (12, 'Заявка'), (5, 'Квартиль'), (1, 'Ксерокопия'), (3, 'Монография'), (2, 'Скриншот'), (7, 'Патент'), (11, 'Приказ'), (6, 'Процентиль'), (4, 'Публикация'), (10, 'Распоряжение'), (8, 'Свидетельство'), (17, 'Свидетельство об аккредитации'), (19, 'Сертификат'), (14, 'Служебная записка'), (9, 'Справка'), (15, 'Справка о внедрении'), (21, 'Удостоверение')], verbose_name='Тип файла'),
        ),
    ]
