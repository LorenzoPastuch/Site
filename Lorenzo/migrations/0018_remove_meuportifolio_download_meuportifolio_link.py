# Generated by Django 4.2.4 on 2023-08-23 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lorenzo', '0017_infos_nivel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meuportifolio',
            name='download',
        ),
        migrations.AddField(
            model_name='meuportifolio',
            name='link',
            field=models.CharField(default='link', max_length=50),
            preserve_default=False,
        ),
    ]
