from django.db import models
from django.conf import settings
from imagr_user.models import ImagrUser, Relationships
from django.core.urlresolvers import reverse
from django.template.defaultfilters import escape


privacy_choices = ((0, 'Private'), (1, 'Shared'), (2, 'Public'))

class Photo(models.Model):
    image_upload_folder = 'photos/%Y/%m/%d'
    image = models.ImageField(upload_to=image_upload_folder,
                              height_field='height',
                              width_field='width')
    height = models.PositiveIntegerField(default=0, editable=False)
    width = models.PositiveIntegerField(default=0, editable=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='photo_owner')
    title = models.CharField(max_length=127)
    description = models.CharField(max_length=127)
    date_uploaded = models.DateTimeField(auto_now_add=True, blank=False)
    date_modified = models.DateTimeField(auto_now=True, blank=False)
    date_published = models.DateTimeField(auto_now=True)
    privacy_option = models.IntegerField(choices=privacy_choices)
    size = models.PositiveIntegerField(default=0, editable=False)
    size_range = models.CharField(max_length=27, editable=False, blank=False)


    class Meta:
        ordering = ['title', 'description']

    def __unicode__(self):
        return self.description

    def owner_link(self):
        return '<a href="%s">%s</a>' % (reverse(
            "admin:imagr_user_imagruser_change", args=(self.owner.id,)), escape(self.owner))

    owner_link.allow_tags = True
    owner_link.short_description = "Owner"


    def save(self, *args, **kwargs):
        self.size = self.image.size

        if self.size < 1000001:
            self.size_range = '<= 1MB'
        elif self.size < 10000001:
            self.size_range = '<= 10MB'
        elif self.size < 100000001:
            self.size_range = '<= 100MB'
        else:
            self.size_range = '> 100MB'

        super(Photo, self).save(*args, **kwargs)


class Album(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='Album_owner')
    title = models.CharField(max_length=127)
    description = models.CharField(max_length=127)
    photos = models.ManyToManyField(
        Photo,
        related_name='album_photo',
        blank=True,
        null=True)
    date_uploaded = models.DateTimeField(auto_now_add=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True)
    date_published = models.DateTimeField(auto_now=True, blank=True)
    privacy_option = models.IntegerField(choices=privacy_choices)
    cover_photo = models.ManyToManyField(
        Photo,
        related_name='cover_photo',
        blank=True,
        null=True)


    class Meta:
        abstract = False
        ordering = ['title', 'description']

    def __unicode__(self):
        return self.description

    def owner_link(self):
        return '<a href="%s">%s</a>' % (reverse(
            "admin:imagr_user_imagruser_change", args=(self.owner.id,)), escape(self.owner))

    owner_link.allow_tags = True
    owner_link.short_description = "User"

