from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns('blog.views',
    url(r'^$', 'index', name='index'),
    url(r'^post/(?P<pk>\d+)/$', 'post', name='post'),
)