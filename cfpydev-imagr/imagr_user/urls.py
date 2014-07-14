from django.conf.urls import patterns, url
from imagr_user import views

urlpatterns = patterns('',
                       url(r'^(?P<user_id>\d+)/$',
                           views.home,
                           name='home'),)
