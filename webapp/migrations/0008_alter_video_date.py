# Generated by Django 4.0.1 on 2022-07-22 08:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_alter_video_date_alter_video_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='date',
            field=models.DateField(verbose_name=datetime.datetime(2022, 7, 22, 14, 27, 29, 775528)),
        ),
    ]
