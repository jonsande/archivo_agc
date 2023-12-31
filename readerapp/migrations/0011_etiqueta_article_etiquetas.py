# Generated by Django 4.1.7 on 2023-04-08 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readerapp', '0010_remove_article_borrame'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='etiquetas',
            field=models.ManyToManyField(to='readerapp.etiqueta'),
        ),
    ]
