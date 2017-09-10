from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="home"),

    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]
