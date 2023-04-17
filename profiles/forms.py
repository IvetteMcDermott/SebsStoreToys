from .models import UserProfile
from django import forms
from django.forms import fields, ModelForm


class ProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', )
