from .models import Ware, WareImage
from django import forms
from django.forms import fields, ModelForm


class WareForm(forms.ModelForm):
    # Form will be as crispy with labels as it is better for fill the wares in
    class Meta:
        model = Ware
        fields = ('name', 'sku', 'description', 'price', 'new', 'clearance', 'incomming', 'subcategory', 'height', 'width', 'length', )


class ImageForm(forms.ModelForm):
    # Form will be as crispy with labels as it is better for fill the wares in
    class Meta:
        model = WareImage
        fields = ('ware', 'image', 'caption', )


class Search(forms.ModelForm):
    class Meta:
        model = Ware
        fields = ('name', 'description', )