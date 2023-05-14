from .models import ContactUs
from django import forms
from django.forms import fields, ModelForm


class ContactUsForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = ('email', 'subject', 'name', 'subject', 'description', )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'email': 'Email',
            'subject': 'Subject',
            'name': 'Name',
            'subject': 'Subject',
            'description': 'If you have an order include it at the begin of the message with #',
        }

        self.fields['email'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
