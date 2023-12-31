# Generated by Django 3.1 on 2022-06-04 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0011_banner'),
        ('auth_api', '0015_user_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userposition',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_positions', to='reference.department', verbose_name='Кафедра'),
        ),
        migrations.AlterField(
            model_name='userposition',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_positions', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
