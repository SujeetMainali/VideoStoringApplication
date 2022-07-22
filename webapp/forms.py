from datetime import date
from django.core import validators
from django import forms
from .models import Video
from moviepy.editor import VideoFileClip

def videoLength(value):
    if value.size > 104857600 * 10:
        raise forms.ValidationError('Video file size must be less than 1GB.')
    else:
        return value
# def videotime(value):
#     if value.duration > 60 * 10:
#         raise forms.ValidationError('Video duration must be less than 10 minutes.')
#     else:
#         return value


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description', 'video']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'video': forms.FileInput(attrs={'class': 'form-control'}),
            
        }
        error_messages = {
            'title': {
                'max_length': "Title must be less than 200 characters.",
                'required': "Title is required.",
            },
            'description': {
                'max_length': "Description must be less than 1000 characters.",
                'required': "Description is required.",
            },
            'video': {
                'max_length': "Video file size must be less than 1GB.",
                'required': "Video is required.",
            },
        }

    video = forms.FileField(validators=[videoLength, ])

class VideoDetailsForm(forms.ModelForm):
    size = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    duration = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    type = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Video
        fields = ['title', 'description', 'video']
        
    
    
       
            
           
