# Generated by Django 2.2.3 on 2019-07-11 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190711_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='dislike',
            name='like_or_dislike',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dislike',
            name='preference',
            field=models.BooleanField(default=False),
        ),
    ]