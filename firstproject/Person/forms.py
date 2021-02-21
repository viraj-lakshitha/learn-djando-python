from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = [
            'firstName',
            'lastName',
            'emailAddress'
        ]

class RawPersonForm(forms.Form):
    firstName = forms.CharField()
    firstName = forms.CharField()
    firstName = forms.EmailField()