from django import forms
from .models import MenuModels


class MenuForm(forms.ModelForm):
    class Meta:
        model = MenuModels
        fields = '__all__'