from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django import forms
from .models import Message


class UserRegForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html()
    )
    password2 = forms.CharField(
        label='Пароль (повторно)',
        widget=forms.PasswordInput,
        help_text='Введите пароль повторно для проверки'
    )

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1']:
            password_validation.validate_password(cd['password1'])
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Пароль не подходит')
        return cd['password1']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        labels = {
            'username': 'Имя пользователя',
            'first_name': 'Имя',
            'last_name': 'Фамилия'
        }

class MessageForm(forms.ModelForm):
    
    class Meta:
        model = Message
        fields = ('email', 'text')
