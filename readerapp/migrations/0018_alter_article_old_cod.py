# Generated by Django 4.1.7 on 2023-10-09 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readerapp', '0017_alter_category_name_alter_category_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='old_cod',
            field=models.IntegerField(max_length=12, unique=True, verbose_name='Código Viejo'),
        ),
    ]
