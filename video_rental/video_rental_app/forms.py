from django import forms
from .models import Video, Rating
from django.contrib.auth import get_user_model

User = get_user_model()


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        # fields = '__all__'
        fields = ['title', 'description', 'actual_video']


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']
        help_texts = {
            'username': None,
        }


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)