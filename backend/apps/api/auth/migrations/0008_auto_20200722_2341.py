# Generated by Django 3.0.8 on 2020-07-22 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0008_auto_20200707_1152'),
        ('auth_api', '0007_user_category_expert'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='role_expert',
            new_name='is_expert',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='role_manager_department',
            new_name='is_manager_department',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='role_manager_faculty',
            new_name='is_manager_faculty',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='role_super_expert',
            new_name='is_super_expert',
        ),
        migrations.AddField(
            model_name='user',
            name='manager_department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='reference.Department', verbose_name='Кафедра'),
        ),
        migrations.AddField(
            model_name='user',
            name='manager_faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='reference.Faculty', verbose_name='Факультет'),
        ),
        migrations.AlterField(
            model_name='user',
            name='category_expert',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='reference.MainCategory', verbose_name='Категория эксперта'),
        ),
    ]