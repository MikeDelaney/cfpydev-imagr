from django.conf.urls import patterns, url
from imagr_images import views

urlpatterns = patterns('',
            url(r'^(?P<album_id>\d+)/$', views.albumView, name='albums'),
        )
