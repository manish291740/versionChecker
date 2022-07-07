from django import forms
from .models import checkDataModel


class checkForm(forms.ModelForm):
    class Meta:
        model=checkDataModel
        fields= "__all__"