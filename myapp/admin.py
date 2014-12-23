from django.contrib import admin
from myapp.models import Blog, Category, Entry, Comment
from django.conf import settings
from django.db import models
from django import forms

class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}

    def __init__(self, model, admin_site):
        super(BlogAdmin, self).__init__(model, admin_site)


class CommentAdmin(admin.ModelAdmin):
    display_fields = ["post", "author", "created"]


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

    def __init__(self, model, admin_site):
        super(CategoryAdmin, self).__init__(model, admin_site)


class EntryAdmin(admin.ModelAdmin):
    """docstring for ClassName"""
    formfield_overrides = {models.TextField: {'widget': forms.Textarea(attrs={'class': 'ckeditor'})},}
    list_display= ['title']

    class Media():
        js = ('ckeditor/ckeditor.js',)


admin.site.register(Comment, CommentAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)