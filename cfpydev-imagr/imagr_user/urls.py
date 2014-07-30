from django.conf.urls import patterns, url
from imagr_user import views
from imagr_images import views as imagesViews

urlpatterns = patterns('',
                       url(r'^$', views.home, name='home'),
                       )
