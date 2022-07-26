from django.forms import ModelForm
from django import forms
from .models import Feed


class FeedForm(ModelForm):

    address = forms.URLField(widget=forms.URLInput(
        attrs={
            "placeholder": "Enter URL...",
            "class": "form-control form-control-lg"}),
            label='')
    x_path = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder": "Enter XPath...",
            "class": "form-control form-control-lg"}),
            label='')

    class Meta:
        model = Feed
        fields = ['address', 'x_path']
