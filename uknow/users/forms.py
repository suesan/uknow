from django import forms
from users.models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length = 30,
        required   = False,
    )
    password = forms.CharField(
        max_length = 128,
        widget     = forms.PasswordInput,
        required   = False
    )
    class Meta:
        Model = User
        widget = {
            'password': forms.PasswordInput(),
        }
