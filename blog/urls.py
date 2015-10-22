from django.conf.urls import url, patterns
from . import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^blog/(?P<slug>\w.+)', views.post, name='post'),
    url(r'^category/(?P<slug>[^\.]+)', views.category, name='category'),
)