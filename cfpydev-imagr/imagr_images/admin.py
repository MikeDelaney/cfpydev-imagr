from django.contrib import admin
from imagr_images.models import Photo, Album, ImagrUser


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'user_link', 'owner', 'image_size', 'height', 'width')
    list_display_links = ('owner',)
    readonly_fields = ('date_uploaded',
                       'date_modified',
                       'date_published')

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner_link')
    readonly_fields = ('date_uploaded',
                       'date_modified',
                       'date_published')

class ImagrUserAdmin(admin.ModelAdmin):
    search_fields = ['username', 'first_name', 'last_name', 'email']

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(ImagrUser, ImagrUserAdmin)
