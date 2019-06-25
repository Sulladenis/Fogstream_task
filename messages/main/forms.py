from django.contrib.auth.models import User
from django import forms

class UserRegForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
