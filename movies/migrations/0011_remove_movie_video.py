# Generated by Django 4.1.1 on 2022-09-20 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0010_remove_movie_test_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='video',
        ),
    ]
