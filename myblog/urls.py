from django.conf.urls import *
from django.contrib import admin
from myapp.views import *
from tastypie.api import Api
from myapp.api import EntryResource, UserResource

entry_resource = EntryResource()

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(EntryResource())


urlpatterns = patterns('',
                       url(r'^$', index, name='index'),
                       url(r'^blog/(?P<slug>[^\.]+)', view_blog_category.as_view(), name='view_blog_post'),
                       #url(r'^blog/category/(?P<slug>[^\.]+)', 'view_category', name='view_blog_category'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^blog/', include('myapp.urls')),
                       url(r'^add_comment/(\d+)/', view_blog_category.as_view(), name="add_comment"),
                       url(r'^ckeditor/', include('ckeditor.urls')),
                       url(r'^delete/(?P<id>\d+)/$', delete_blog, name='delete_blog'),
                       url(r'^delete_comment/(?P<id>\d+)/', DeleteComment.as_view(), name='delete_comment'),
                       url(r'^signup/', SignUpView.as_view(), name='signup'),
                       url(r'^dashboard/', DashBoardView.as_view(), name='dashboard'),
                       url(r'^login$', LoginView.as_view(), name='login'),
                       url(r'^api/', include(v1_api.urls)),
                       url(r'^logout$', 'django.contrib.auth.views.logout', {"next_page":"/"}, name='logout'),
                       url(r'^addblog/', add_new_blog.as_view(), name='add_blog'),
                       url(r'^editblog/(?P<id>\d+)/$', EditBlog.as_view(), name='edit_blog')
                       # url(r'^/(?P<slug>)', view_blog_category.as_view(), name='view_blog_category'),
                       )

