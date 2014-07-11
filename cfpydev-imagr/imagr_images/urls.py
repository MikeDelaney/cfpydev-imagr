from django.conf.urls import patterns, url

from imagr_images import views

urlpatterns = patterns('',
                       url(r'^$', views.front, name='front'),
                       url(r'^(?P<user_id>\d+)/home/$', views.home, name='home'),
                       )
