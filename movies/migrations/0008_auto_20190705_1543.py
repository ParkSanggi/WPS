# Generated by Django 2.2.3 on 2019-07-05 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_auto_20190705_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='video_file',
            field=models.FileField(upload_to='media/%Y/%m/%d'),
        ),
    ]