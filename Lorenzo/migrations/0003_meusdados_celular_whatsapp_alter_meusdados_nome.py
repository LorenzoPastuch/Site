# Generated by Django 4.2.4 on 2023-08-15 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lorenzo', '0002_meusdados'),
    ]

    operations = [
        migrations.AddField(
            model_name='meusdados',
            name='celular_whatsapp',
            field=models.CharField(default=None, max_length=15),
        ),
        migrations.AlterField(
            model_name='meusdados',
            name='nome',
            field=models.CharField(max_length=30),
        ),
    ]
