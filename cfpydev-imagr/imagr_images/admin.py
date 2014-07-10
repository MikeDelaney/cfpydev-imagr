from django.contrib import admin
from imagr_images.models import Photo, Album, ImagrUser


class PhotoAdmin(admin.ModelAdmin):

    list_display = ('title',
                    'owner_link',
                    'size',
                    'height',
                    'width')

    search_fields = ['owner__username', 'owner__first_name', 'owner__last_name', 'owner__email']

    readonly_fields = ('date_uploaded', 'date_modified', 'date_published',)
    list_filter = ('date_published', 'size_range')

class AlbumAdmin(admin.ModelAdmin):
    search_fields = ['owner__username', 'owner__first_name', 'owner__last_name', 'owner__email']
    list_display = ('title', 'owner_link')
    readonly_fields = ('date_uploaded',
                       'date_modified',
                       'date_published')

class ImagrUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')
    search_fields = ['username', 'first_name', 'last_name', 'email']

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(ImagrUser, ImagrUserAdmin)
