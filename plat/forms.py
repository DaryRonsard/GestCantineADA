from django import forms
from .models import PlatModel


class PlatForms(forms.ModelForm):
    class Meta:
        model = PlatModel
        fields = '__all__'