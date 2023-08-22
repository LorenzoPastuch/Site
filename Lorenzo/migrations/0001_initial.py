# Generated by Django 4.2.4 on 2023-08-15 20:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MinhaHistoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('historia', models.TextField(max_length=1000)),
                ('data_atualizacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('imagem', models.ImageField(upload_to='imagens')),
            ],
        ),
    ]
