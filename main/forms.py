from django import forms
from .models import Request
from django.forms import TextInput, Textarea, ModelForm, CheckboxInput


class NewRequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ('name', 'description', 'resume')
        widgets = {
            "description": Textarea(attrs={'rows': '1'}),
            'resume': CheckboxInput()
        }