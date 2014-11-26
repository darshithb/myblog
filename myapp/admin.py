from django.contrib import admin
from myapp.models import Blog, Category
from django.conf import settings


class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}

    def __init__(self, model, admin_site):
        super(BlogAdmin, self).__init__(model, admin_site)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

    def __init__(self, model, admin_site):
        super(CategoryAdmin, self).__init__(model, admin_site)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)