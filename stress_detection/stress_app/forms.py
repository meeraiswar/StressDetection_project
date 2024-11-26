# stress_app/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import StressData

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        widgets = {
            'password': forms.PasswordInput(),
        }
        

class StressDataForm(forms.ModelForm):
    class Meta:
        model = StressData
        fields = ['snoring_rate', 'limb_movement', 'eye_movement', 'sleeping_hours',
                  'respiratory_rate', 'body_temperature', 'heart_rate', 'blood_oxygen']
