from django.conf.urls import url
from . import views

app_name = 'core'

urlpatterns = [
    url(r'^$', views.homeview, name="home-core"),
    url(r'^sendEmail$', views.sendEmail, name="sendEmail"),
    url(r'^emailSent$', views.emailSent, name="emailSent"),
]
