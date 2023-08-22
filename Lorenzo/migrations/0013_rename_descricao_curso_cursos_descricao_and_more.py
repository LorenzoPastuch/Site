# Generated by Django 4.2.4 on 2023-08-17 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lorenzo', '0012_rename_descricao_cursos_descricao_curso_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cursos',
            old_name='descricao_curso',
            new_name='descricao',
        ),
        migrations.RenameField(
            model_name='cursos',
            old_name='nome_curso',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='experiencias',
            old_name='descricao_exp',
            new_name='descricao',
        ),
        migrations.RenameField(
            model_name='experiencias',
            old_name='nome_experiencia',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='formacao',
            old_name='descricao_formacao',
            new_name='descricao',
        ),
        migrations.RenameField(
            model_name='formacao',
            old_name='nome_formacao',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='infos',
            old_name='descricao_info',
            new_name='descricao',
        ),
        migrations.RenameField(
            model_name='infos',
            old_name='nome_info',
            new_name='nome',
        ),
    ]
