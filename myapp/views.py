from django.shortcuts import render
from myapp.models import Blog, Category
from django.shortcuts import render_to_response, get_object_or_404
import datetime
from django.views.generic import TemplateView, FormView
from myapp.forms import BlogForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse


def index(request):

    form = BlogForm(request.POST or None)

    dt = Blog.objects.all()
    now = datetime.datetime.now()
    now = datetime.date(now.year, now.month, now.day)
    op1 = []
    for obj in dt:
        diff = now - obj.posted
        op1.append([obj, str(diff)])

    #     date_now = datetime.datetime.now()
    #     diff = date_now.year, date_now.month, date_now.day
    #     obj = dt.posted
    #     datetime.timedelta(date_now - obj)
    #
    # print op1
    op2 = Blog.objects.all().order_by('-posted')
    return render_to_response('index.html', {
        'categories': Category.objects.all()[:],
        'posts': op1,
        op2
    })


def view_post(request, slug):
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })


def view_category(request, slug):
    Category_list = get_object_or_404(Category, slug=slug)

    return render_to_response('view_category.html', {
        'category': Category_list,
        'posts': Blog.objects.filter(category=Category)[:5]
    })


class view_blog_category(TemplateView):
    template_name = "view_blog.html"

    def render_to_response(self, context, **response_kwargs):
        # print context.get('slug')
        obj = Blog.objects.filter(slug=context.get('slug'))
        context['obj'] = obj[0]
        return self.response_class(
            request=self.request,
            template=self.get_template_names(),
            context=context,
            **response_kwargs
        )


class add_new_blog(FormView):
    template_name = "Blog_entry.html"
    form_class = BlogForm

    def get(self, request, *args, **kwargs):

        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            title = form.cleaned_data['title']
            category = form.cleaned_data['category']
            body = form.cleaned_data['body']

            slug = title.replace(" ", "-")
            blog = Blog.objects.create(first_name=first_name, title=title, category=category, body=body, slug=slug)

            return HttpResponseRedirect(reverse("index"))

        else:

            form_class = self.get_form_class()
            form = self.get_form(form_class)
            return self.render_to_response(self.get_context_data(form=form))