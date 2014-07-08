from django.contrib import admin
from imagr_images.models import Photo, Album, ImagrUser

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')
    list_display_links = ('user',)
    readonly_fields = ('date_uploaded',
                               'date_modified',
                               'date_published')


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner')
    list_display_links = ('owner',)


class ImagrUserAdmin(admin.ModelAdmin):
    search_fields = ['username', 'first_name', 'last_name', 'email']

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(ImagrUser, ImagrUserAdmin)

