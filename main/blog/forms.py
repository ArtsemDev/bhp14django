from django.forms import Form, ModelForm, EmailField, CharField, Textarea

from .models import Category


class FeedbackForm(Form):
    email = EmailField()
    text = CharField(widget=Textarea)


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ("name", "slug")
