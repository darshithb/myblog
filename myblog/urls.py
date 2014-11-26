from django.conf.urls import *
from django.contrib import admin
from myapp.views import *
from tastypie.api import Api
from myapp.api import EntryResource, UserResource
# from myapp import views

entry_resource = EntryResource()

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(EntryResource())


urlpatterns = patterns('',
                       url(r'^$', index),
                       url(r'^blog/(?P<slug>[^\.]+)', view_blog_category.as_view(), name='view_blog_post'),
                       #url(r'^blog/category/(?P<slug>[^\.]+)', 'view_category', name='view_blog_category'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^blog/', include('myapp.urls')),
                       url(r'^api/', include(v1_api.urls)),
                       # url(r'^/(?P<slug>)', view_blog_category.as_view(), name='view_blog_category'),
                       )
