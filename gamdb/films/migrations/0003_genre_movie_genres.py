# Generated by Django 4.1.7 on 2023-03-21 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_director_alter_movie_year_movie_director'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(blank=True, null=True, to='films.genre'),
        ),
    ]
