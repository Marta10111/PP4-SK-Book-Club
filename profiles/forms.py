from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):

    profile_image = forms.FileField(label='Image')
    favourite_place = forms.CharField(
                                    label='Favourite Book:',
                                    required=False,
                                    max_length=300)

    class Meta:
        model = UserProfile
        fields = (
            'profile_image',
            'favourite_book'
        )