
from django.contrib.auth.models import User
from django import forms

class UserRegForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput,
    #                            help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Пароль (повторно)',
                                widget=forms.PasswordInput,
                                help_text='Введите пароль повторно для проверки')
                                
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.VaidationError('Пароль не подходит')
        return cd['password2']

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
