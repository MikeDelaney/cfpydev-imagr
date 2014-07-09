from django.contrib import admin
from imagr_images.models import Photo, Album, ImagrUser



class PhotoAdmin(admin.ModelAdmin):

    list_display = ('title',
                    'owner_link',
                    'size',
                    'height',
                    'width')

    search_fields = ['title', 'size']
    readonly_fields = ('date_uploaded', 'date_modified', 'date_published',)
    date_hierarchy = 'date_published'

class AlbumAdmin(admin.ModelAdmin):
    search_fields = ['username', 'first_name', 'last_name', 'email']
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
