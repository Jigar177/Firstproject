from django import forms
from .models import patients

class Patientsform(forms.ModelForm):
    class Meta:
        model=patients
        fields='__all__'
