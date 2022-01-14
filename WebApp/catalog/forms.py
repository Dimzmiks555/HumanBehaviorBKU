from django.core.exceptions import ValidationError
import datetime  # for checking renewal date range.

from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('file', )
