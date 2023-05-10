from .models import NewsBlog
from django import forms
from django.forms import fields, ModelForm


class NewsForm(forms.ModelForm):
    # Form will be as crispy with labels as it is better for fill the wares in
    class Meta:
        model = NewsBlog
        fields = ('title', 'image', 'description', 'source', )