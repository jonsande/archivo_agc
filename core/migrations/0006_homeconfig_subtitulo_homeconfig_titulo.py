# Generated by Django 4.1.7 on 2023-10-17 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_homeconfig_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeconfig',
            name='subtitulo',
            field=models.TextField(default='Bienvenidos al Archivo de Tertulias de Agustín García Calvo', max_length=64),
        ),
        migrations.AddField(
            model_name='homeconfig',
            name='titulo',
            field=models.TextField(default='Archivo de Tertulias de ¿Agustín García Calvo?', max_length=48),
        ),
    ]
