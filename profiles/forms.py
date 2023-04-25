from .models import UserProfile
from django import forms
from django.forms import fields, ModelForm


class ProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('full_name', 'email', 'phone_number', 'country', 'postcode', 'town_or_city', 'street_address1', 'street_address2', 'county' )

    # def __init__(self, *args, **kwargs):
    #     """
    #     Add placeholders and classes, remove auto-generated
    #     labels and set autofocus on first field
    #     """
    #     super().__init__(*args, **kwargs)
    #     placeholders = {
    #         'full_name': 'full_name',
    #         'phone_number': 'Phone Number',
    #         'email': 'email',
    #         'postcode': 'Postal Code',
    #         'town_or_city': 'Town or City',
    #         'street_address1': 'Street Address 1',
    #         'street_address2': 'Street Address 2',
    #         'county': 'County, State or Locality',
    #     }

    #     self.fields['phone_number'].widget.attrs['autofocus'] = True
    #     for field in self.fields:
    #         if field != 'country':
    #             if self.fields[field].required:
    #                 placeholder = f'{placeholders[field]} *'
    #             else:
    #                 placeholder = placeholders[field]
    #             self.fields[field].widget.attrs['placeholder'] = placeholder
    #         self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
    #         self.fields[field].label = False
