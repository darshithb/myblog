# from django.shortcuts import render
from myapp.models import Blog, Category
from django.shortcuts import render_to_response, get_object_or_404, render
import datetime
import arrow
from django.forms.models import model_to_dict
from django.core.context_processors import csrf
from django.views.generic import TemplateView, FormView
from myapp.forms import *
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.models import make_password


def index(request):

    # form = BlogForm(request.POST or None)

    all_blog = Blog.objects.all()
    all_blog = all_blog.order_by('-posted')

    utc = arrow.utcnow()
    time_z = utc.to('local')
    op1 = []
    for obj in all_blog:
        diff = time_z.replace(second=obj.posted.second, minute=obj.posted.minute, hour=obj.posted.hour,
                              day=obj.posted.day, month=obj.posted.month, year=obj.posted.year).humanize()
        op1.append([obj, str(diff)])

    return render_to_response('index.html', {
        'categories': Category.objects.all()[:5],
        'posts': op1, "user": request.session.get('USER_ID')
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

    import pdb

    def render_to_response(self, context, **response_kwargs):
        # print context.get('slug')

        form = CommentForm()
        obj = Blog.objects.filter(slug=context.get('slug'))
        context['obj'] = obj[0]
        context['user'] = self.request.session.get('USER_ID')
        context['form'] = form
        context['comments'] = Comment.objects.filter(post=obj[0])
        return self.response_class(
            request=self.request,
            template=self.get_template_names(),
            context=context,
            **response_kwargs
        )

    def post(self, request, pk):
        """Single post with comments and a comment form."""

        post = Blog.objects.get(pk=int(pk))
        user_id = self.request.session.get('USER_ID')
        user = User.objects.get(pk=user_id)
        body = self.request.POST.get('body')
        comments = Comment.objects.create(post=post, author=user, body=body)

        d = model_to_dict(post)
        return self.render_to_response(d)


class add_new_blog(FormView):
    template_name = "Blog_entry.html"
    form_class = BlogForm

    def get(self, request, *args, **kwargs):

        form = self.form_class(request.POST)

        if request.session.get('USER_ID'):
            form_class = self.get_form_class()
            form = self.get_form(form_class)
            return self.render_to_response(self.get_context_data(form=form))

        next = reverse('index')

        if next is not None:
            return HttpResponseRedirect(next)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        #import pdb
        #pdb.set_trace()

        if form.is_valid():

            first_name = request.session.get('USER_NAME')
            user = request.session.get('USER_ID')
            user = User.objects.get(pk=user)
            title = form.cleaned_data['title']
            category = form.cleaned_data['category']
            body = form.cleaned_data['body']
            slug = title.replace(" ", "-")

            blog = Blog.objects.create(first_name=first_name, title=title, category=category,
                                       body=body, slug=slug, user=user)

            return HttpResponseRedirect(reverse("index"))

        else:
            form_class = self.get_form_class()
            form = self.get_form(form_class)
            return self.render_to_response(self.get_context_data(form=form))


class LoginView(FormView):

    template_name = 'login.html'
    form_class = LoginForm

    def post(self, request, *args, **kwargs):
        """
        Would help to validate user and login the user.
        """

        form = self.form_class(request.POST or None)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                request.session['USER_ID'] = user.pk
                request.session['USER_NAME'] = user.first_name

                return HttpResponseRedirect(reverse('dashboard'))

            messages.error(request, "Wrong username and Password combination.")
            return self.form_invalid(form)

        else:
            return self.form_invalid(form)

    def get(self, request, *args, **kwargs):

        if request.session.get('USER_ID', ''):
            next = reverse('dashboard')

            if next is not None:
                return HttpResponseRedirect(next)

        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(self.get_context_data(form=form))


class SignUpView(FormView):

    template_name = 'signup.html'
    form_class = SignUpForm

    def post(self, request, *args, **kwargs):
        """
        Would help to validate user and login the user.
        """

        data = {}
        form = self.form_class(request.POST)
        # import pdb
        # pdb.set_trace()
        if form.is_valid():
            data['first_name'] = form.cleaned_data['first_name']
            data['last_name'] = form.cleaned_data['last_name']
            data['email'] = form.cleaned_data['email']
            data['username'] = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password_cnf = form.cleaned_data['password_cnf']

            if password == password_cnf:
                try:
                    data['password'] = make_password(password, salt="blog")
                    user = User.objects.create(**data)
                except:
                    import sys
                    print sys.exc_value
                    # user.delete()
                    messages.error(request, "Something went wrong. Please try again.")
                    return self.form_invalid(form)

            else:
                messages.error(request, "Passwords did not match.")
                return self.form_invalid(form)

            if user is not None:
                user = authenticate(username=data['username'], password=password)
                login(request, user)
                request.session['USER_ID'] = user.pk
                request.session['USER_NAME'] = user.first_name

                return HttpResponseRedirect(reverse('index'))
            messages.error(request, "Wrong username and Password combination.")
            return self.form_invalid(form)

        else:
            return self.form_invalid(form)

    def get(self, request, *args, **kwargs):

        if request.session.get('USER_ID', ''):
            next = reverse('index')

            if next is not None:
                return HttpResponseRedirect(next)

        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(self.get_context_data(form=form))


class DashBoardView(TemplateView):

    template_name = 'dashboard.html'

    def filtered_blogs(request, user_id):

        # user_id = request.session.get('USER_ID', '')
        f_blog = Blog.objects.all().filter(user=user_id)
        f_blog = f_blog.order_by('-posted')

        return f_blog

    def render_to_response(self, context, **response_kwargs):

        user_id = self.request.session.get('USER_ID', '')
        # user = User.objects.get(pk=user_id)
        context['name'] = self.request.session.get('USER_NAME', '')
        context['blog'] = self.filtered_blogs(user_id)

        return self.response_class(
            request=self.request,
            template=self.get_template_names(),
            context=context,
            **response_kwargs
        )


def delete_blog(request, *args, **kwargs):
    user_id = request.session.get('USER_ID', '')
    next = reverse('dashboard')
    id = int(kwargs['id'])
    inst = Blog.objects.get(pk=id)
    user = User.objects.get(pk=user_id)

    if inst.first_name == user.first_name:
        inst.delete()
        return HttpResponseRedirect(next)
    else:
        next = reverse('view_blog_post', args=[str(inst.slug)])
        messages.error(request, "Sorry, you're not the author of this Blog.")
        return HttpResponseRedirect(next)


def delete_comment(request, **kwargs):
    user_id = request.session.get('USER_ID')
    id = int(kwargs['id'])
    inst = Comment.objects.get(pk=id)
    user = User.objects.get(pk=user_id)
    post = Blog.objects.get(pk=inst.post_id)
    next = reverse('view_blog_post', args=[str(post.slug)])

    if post.user_id == user_id or inst.author_id == user_id:
        inst.delete()
        messages.add_message(request, messages.SUCCESS, "Comment deleted successfully.")
        return HttpResponseRedirect(next)

    else:
        messages.add_message(request, messages.ERROR, "Sorry, you're not the author of this blog or this comment.")
        return HttpResponseRedirect(next)




