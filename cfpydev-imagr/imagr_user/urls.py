from django.conf.urls import patterns, url
from imagr_user import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
)
