# Generated by Django 4.1.1 on 2022-09-25 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0022_alter_movie_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.CharField(choices=[('Action & Adventure', 'Action & Adventure'), ('Comedies', 'Comedies'), ('Drama', 'Drama'), ('Blockbuster Movies', 'Blockbuster Movies'), ('Popular Movies', 'Popular Movies')], max_length=100),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tags',
            field=models.CharField(choices=[('Top10', 'Top10'), ('Exciting Movies', 'Exciting Movies'), ('Critically Acclaimed Films', 'Critically Acclaimed Films'), ('Familiar Favorites', 'Familiar Favorites'), ('Top10IMDb', 'Top10IMDb')], max_length=50),
        ),
    ]