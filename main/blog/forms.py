from django.forms import Form, ModelForm, EmailField, CharField, Textarea, EmailInput, TextInput

from .models import Category


class FeedbackForm(Form):
    email = EmailField(
        widget=EmailInput(
            attrs={
                "class": "form-control",
                "id": "email",
                "placeholder": "Enter your email..."
            }
        )
    )
    message = CharField(
        widget=Textarea(
            attrs={
                "class": "form-control",
                "style": "height: 12rem",
                "id": "message",
                "placeholder": "Enter your message..."
            }
        )
    )
    name = CharField(
        widget=TextInput(
            attrs={
                "class": "form-control",
                "id": "name",
                "placeholder": "Enter your name..."
            }
        )
    )


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ("name", "slug")
