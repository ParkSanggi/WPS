# Generated by Django 2.2.3 on 2019-07-19 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_auto_20190717_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='vertical_sample_video_file',
            field=models.FileField(blank=True, null=True, upload_to='media/movie/<django.db.models.fields.CharField>/sample_video'),
        ),
    ]
