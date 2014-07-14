from django.contrib import admin
from imagr_images.models import Photo, Album


class PhotoAdmin(admin.ModelAdmin):

    list_display = ('title',
                    'owner_link',
                    'size',
                    'height',
                    'width')

    search_fields = ['owner__username', 'owner__first_name', 'owner__last_name', 'owner__email']

    readonly_fields = ('id', 'date_uploaded', 'date_modified', 'date_published',)
    list_filter = ('date_published', 'size_range')

class AlbumAdmin(admin.ModelAdmin):
    search_fields = ['owner__username', 'owner__first_name', 'owner__last_name', 'owner__email']
    list_display = ('id', 'title', 'owner_link')
    readonly_fields = ('date_uploaded',
                       'date_modified',
                       'date_published')



admin.site.register(Photo, PhotoAdmin)
admin.site.register(Album, AlbumAdmin)