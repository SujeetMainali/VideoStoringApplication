from datetime import datetime
from distutils import core
from email import message
from django.db import models
# from django.core.validators import FileExtensionValidator
from django.core import validators

def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.mp4', '.mkv']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(default=datetime.now)
    video = models.FileField(upload_to='videos/', validators=[validate_file_extension], error_messages={'unsupported file': 'Only mp4 or mkv file type is supported.'})
    

    def __str__(self):
        return self.title
    
