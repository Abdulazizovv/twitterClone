# forms.py
from django import forms
from .models import Tweet, UserProfile

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'What\'s happening?'}),
        }

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user', 'bio', 'profile_picture']