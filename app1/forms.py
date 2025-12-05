from django import forms
from .models import Voter

class VoterForm(forms.ModelForm):
    class Meta:
        model = Voter
        fields = ['full_name', 'father_name', 'dob', 'gender', 'address', 'photo']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.Select(choices=[
                ('Male', 'Male'),
                ('Female', 'Female'),
                ('Other', 'Other'),
            ])
        }
