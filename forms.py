from django import forms

from picsApp.models import Photo


class PostForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('images')
