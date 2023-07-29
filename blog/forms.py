from .models import Newa
from django.forms import ModelForm, TextInput, Textarea,TimeInput


class NewForm(ModelForm):
    class Meta:
        model = Newa
        fields = ['title','text']

        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Заголовок квака",
            }),
            'text': Textarea(attrs={
                'class': "form-control",
                'placeholder': "Квакнуть",
            }),
        }