from .models import Review
from django import forms
from django.forms import fields, ModelForm


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('body', 'rating', )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'body': 'Your review',
        }

        self.fields['body'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'rating':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
