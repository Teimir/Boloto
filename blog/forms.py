from .models import Post, User
from django.forms import ModelForm, TextInput, Textarea, PasswordInput, EmailInput


class NewForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','text', 'author']

        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Заголовок квака",
            }),
            'text': Textarea(attrs={
                'class': "form-control",
                'placeholder': "Квакнуть",
            })
        }

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password']

        widgets = {
            'username': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Username",
            }),
            'password': PasswordInput(attrs={
                'class': "form-control",
                'placeholder': "Password",
            }),
        }

class SignupForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password', "email"]

        widgets = {
            'username': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Username",
            }),
            'password': PasswordInput(attrs={
                'class': "form-control",
                'placeholder': "Password",
            }),

            'email': EmailInput(attrs={
                'class': "form-control",
                'placeholder': "billyHarrington@gay.website",
            }),
        }