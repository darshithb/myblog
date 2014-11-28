__author__ = 'darshithb'

from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': "Enter First Name", 'class': 'form-control'}),
            'title': forms.TextInput(attrs={'placeholder': "Enter Title", 'class': 'form-control'}),
            'body': forms.Textarea(attrs={'placeholder': "Enter Body", 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.fields['slug'].required = False
