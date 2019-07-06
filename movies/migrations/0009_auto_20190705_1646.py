# Generated by Django 2.2.3 on 2019-07-05 07:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_auto_20190705_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='production',
            field=models.DateField(default=datetime.datetime(2019, 7, 5, 7, 45, 16, 678811, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='movie',
            name='running_time',
            field=models.CharField(default='2000-01-01', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='uploaded',
            field=models.DateField(default=datetime.datetime(2019, 7, 5, 7, 45, 16, 678830, tzinfo=utc)),
        ),
    ]