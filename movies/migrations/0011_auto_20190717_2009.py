# Generated by Django 2.2.3 on 2019-07-17 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0010_auto_20190716_2242'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moviecontinue',
            old_name='movie_id',
            new_name='movie',
        ),
        migrations.RenameField(
            model_name='moviecontinue',
            old_name='sub_user_id',
            new_name='sub_user',
        ),
    ]
