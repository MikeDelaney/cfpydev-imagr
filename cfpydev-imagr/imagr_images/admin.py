from django.contrib import admin
from imagr_images.models import Photo, Album, ImagrUser

# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
    fields = ( 'title', 'description', 'image' )

admin.site.register(Photo, PhotoAdmin)