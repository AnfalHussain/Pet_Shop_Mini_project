from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        exclude = ["available"]

class UpdatePetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = "__all__"