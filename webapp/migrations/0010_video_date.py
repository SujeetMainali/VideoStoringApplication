# Generated by Django 4.0.1 on 2022-07-22 08:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_remove_video_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
