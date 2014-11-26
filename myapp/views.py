from django.shortcuts import render
from myapp.models import Blog, Category
from django.shortcuts import render_to_response, get_object_or_404
import datetime
from django.views.generic import TemplateView


def index(request):

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
    return render_to_response('index.html', {
        'categories': Category.objects.all()[:],
        'posts': op1
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
            request = self.request,
            template = self.get_template_names(),
            context = context,
            **response_kwargs
        )