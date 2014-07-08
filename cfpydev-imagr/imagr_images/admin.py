from django.contrib import admin
from imagr_images.models import Photo, Album, ImagrUser

# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
    readonly_fields = ('date_uploaded',
                               'date_modified',
                               'date_published')



