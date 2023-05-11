from .models import ContactUs
from django import forms
from django.forms import fields, ModelForm


class ContactUsForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = ('email', 'subject', 'name', 'subject', 'description', )
