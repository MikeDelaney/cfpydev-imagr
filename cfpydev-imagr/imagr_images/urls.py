from django.conf.urls import patterns, url, include
from imagr_images import views

urlpatterns = patterns('',
    url(r'^(?P<album_id>\d+)/$', views.albumView, name='albums'),
    url(r'^home/', include('imagr_user.urls')),
    url(r'^photo/(?P<photo_id>\d+)/$', views.photoView, name='photo'),
    # url(r'^stream/(?P<user_id>\d+)/$', views.streamView, name='stream'),
    )
