# Generated by Django 4.2.1 on 2023-05-17 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0007_alter_actor_description_alter_comment_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='photo_url',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(blank=True, to='films.genre'),
        ),
    ]
