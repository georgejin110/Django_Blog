from django.conf.urls import url, patterns
# from . import views


urlpatterns = patterns('',
    url(r'^$', 'blog.views.index', name='index'),
    url(r'^blog/(?P<slug>[^\.]+)/$', 'blog.views.post', name='post'),
    url(r'^category/(?P<slug>[^\.]+)', 'blog.views.category', name='category'),
)