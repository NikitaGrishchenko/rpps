# Generated by Django 3.1 on 2022-02-09 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questioning', '0026_categoryquestionnaire_max_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryquestionnaire',
            name='main_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='main_category', to='questioning.maincategoryquestionnaire', verbose_name='Главная категория'),
        ),
        migrations.AlterField(
            model_name='categoryquestionnaireuser',
            name='category_questionnaire',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_questionnaire', to='questioning.categoryquestionnaire', verbose_name='Категория анкеты'),
        ),
    ]
