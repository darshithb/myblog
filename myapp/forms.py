__author__ = 'darshithb'

from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog

        widgets={
            'first_name': forms.TextInput(attrs={'placeholder': "Enter First Name"}),
            'title': forms.TextInput(attrs={'placeholder': "Enter Title"}),
            'body': forms.Textarea(attrs={'placeholder': "Enter Body"}),
        }
        # self.fields['first_name'].placeholder = "Enter your first name"
        # self.fields['title'].placeholder = "Title"
        # self.fields['category'].placeholder = "Enter your Body here"

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.fields['slug'].required = False


        # title = title(widget=forms.TextInput(attrs={'placeholder': 'Title'}))