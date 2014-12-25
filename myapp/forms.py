__author__ = 'darshithb'

from django import forms
from .models import Blog, Comment
from ckeditor.widgets import CKEditorWidget
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


class BlogForm(forms.ModelForm):

    first_name = forms.CharField(max_length=20, required=False)

    class Meta:
        model = Blog
        exclude= ['user',]

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': "Enter First Name", 'class': 'form-control'}),
            'title': forms.TextInput(attrs={'placeholder': "Enter Title", 'class': 'form-control'}),
            'body': forms.Textarea(attrs={'placeholder': "Enter Body", 'id': 'blog-body', 'class': 'form-control'}),
        }

        body = forms.CharField(widget=CKEditorWidget())

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.fields['slug'].required = False
        self.fields['first_name'].widget = forms.HiddenInput()


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment

    def add_comment(request, pk):
        """Add a new comment."""

        p = request.Post

        if "body" in p and p["body"]:
            author = "Anonymous"

            if p["author"]:
                author = p["author"]

            comment = Comment(post=Blog.objects.get(pk=pk))
            cf = CommentForm(p, instance=comment)
            cf.fields["author"].required = False

            comment = cf.save(commit=False)
            comment.author = author
            comment.save()

        return HttpResponseRedirect(reverse("dbe.blog.views.post", args=[pk]))


class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'type': 'text',
                                                                            'placeholder': 'Enter your username',
                                                                            'class': 'span'
    }))
    password = forms.CharField(required=True, max_length=20, widget=forms.TextInput(attrs={'type': 'password',
                                                                                           'placeholder': 'Password',
                                                                                           'class': 'span'
    }))


class SignUpForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': 'text', 'placeholder': 'Enter your First Name', 'class': 'span'
    }))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': 'text', 'placeholder': 'Enter your Last Name', 'class': 'span'
    }))
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': 'text', 'placeholder': 'Create your Username', 'class': 'span'
    }))
    email = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': 'email', 'placeholder': 'Enter your Email', 'class': 'span'
    }))
    password = forms.CharField(
        max_length=20, widget=forms.TextInput(attrs={
            'type': 'password', 'placeholder': 'Password', 'class': 'span'
    }))
    password_cnf = forms.CharField(
        max_length=20, widget=forms.TextInput(attrs={
            'type': 'password', 'placeholder': 'Re-enter Password', 'class': 'span'
    }))
