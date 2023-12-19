# Generated by Django 3.0.8 on 2020-07-31 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0009_auto_20200731_1410'),
        ('auth_api', '0008_auto_20200722_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userposition',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_positions', to='reference.Department', verbose_name='Кафедра'),
        ),
    ]