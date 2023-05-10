from .models import Review
from django import forms
from django.forms import fields, ModelForm


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('body',)