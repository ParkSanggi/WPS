# Generated by Django 2.2.3 on 2019-07-09 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('movies', '0007_auto_20190709_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieContinue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_be_continue', models.TimeField()),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_continue', to='movies.Movie')),
                ('sub_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_continue', to='accounts.SubUser')),
            ],
        ),
    ]
