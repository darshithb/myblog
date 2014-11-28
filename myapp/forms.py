__author__ = 'darshithb'

from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': "Enter First Name"}),
            'title': forms.TextInput(attrs={'placeholder': "Enter Title"}),
            'body': forms.Textarea(attrs={'placeholder': "Enter Body"}),
        }

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.fields['slug'].required = False
