# Generated by Django 2.2.3 on 2019-07-05 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='parent_genre',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_genre', to='movies.Genre'),
        ),
    ]