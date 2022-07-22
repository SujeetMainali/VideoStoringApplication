# Generated by Django 4.0.1 on 2022-07-22 08:37

from django.db import migrations, models
import webapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_alter_video_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(error_messages={'unsupported file': 'Only mp4 or mkv file type is supported.'}, upload_to='videos/', validators=[webapp.models.validate_file_extension]),
        ),
    ]