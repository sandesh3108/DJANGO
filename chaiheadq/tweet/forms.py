from django import forms
from .models import tweet

class tweetforms(forms.ModelForm):
    class Meta:
        model=tweet
        filds=['text','photo']
        # we take text and photo bacause we take it in moduls.py file