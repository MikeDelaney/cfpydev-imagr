from django.contrib import admin
from imagr_images.models import Photo, Album, ImagrUser

# Register your models here.


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'user_link','size')


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner_link')


class ImagrUserAdmin(admin.ModelAdmin):
    search_fields = ['username', 'first_name', 'last_name', 'email']

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(ImagrUser, ImagrUserAdmin)
