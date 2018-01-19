from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'letter/(?P<letter>[A-Z])/$', views.index, name='index'),
    url(r'color/(?P<color>[\w]+)/$', views.index, name='index'),
    url(r'category/(?P<category>[-\w]+)/$', views.index, name='index'),
    url(r'(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'search/$', views.mineral_search, name='search'),
]
