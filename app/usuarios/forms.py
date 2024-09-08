from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        labels = {
            'username': 'Nome de usuário',
            'password1': 'Senha',
            'password2': 'Confirmação da senha',
        }
        help_texts = {
            'username': '',
            'password1': (
                'Sua senha deve conter pelo menos 8 caracteres. '
                'Sua senha não pode ser totalmente numérica.'
            ),
            'password2': '',
        }
        error_messages = {
            'password_mismatch': 'As senhas não correspondem.',
        }
