from django.conf.urls import patterns, include, url
from imagr_site import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'imagr_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.front, name='front'),
    url(r'^home/', include('imagr_user.urls')),
    url(r'^album/', include('imagr_images.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
