"""Project forms."""
from django.forms import ModelForm, Textarea, TextInput

from .models import Post


class PostForm(ModelForm):
    """Post Form."""

    class Meta:
        """Form Meta."""

        model = Post
        fields = ['title', 'description', 'content']
        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Название статьи"
            }),
            "description": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Описание статьи"
            }),
            "content": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Содержимое"
            })
        }
