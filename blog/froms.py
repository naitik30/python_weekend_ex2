from django import forms
from .models import BlogData

class BlogDataForm(forms.ModelForm):
    class Meta:
        model = BlogData
        fields = ["title",
                "content",
                "image"]