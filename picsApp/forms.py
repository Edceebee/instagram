from django import forms


class InstagramForm(forms.Form):
    name = forms.CharField()
    instagram_picture = forms.ImageField()
