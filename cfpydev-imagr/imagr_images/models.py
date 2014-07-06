from django.db import models
from django.contrib.auth.models import User


class Photo(models.Model):

    privacy_choices=(('private', 0), ('shared', 1), ('public', 2))
    image_upload_folder = '/Users/eyuelabebe/Desktop/projects/django-imagr/cfpydev-imagr/imagr_images'

    image = models.ImageField(upload_to=image_upload_folder)
    user = models.ForeignKey(User) # we can also do user = models.ForeignKey("django.contrib.auth.models.User")
    title = models.CharField(max_length=127)
    description = models.CharField(max_length=127)
    date_uploaded = models.DateTimeField(auto_now_add=True, blank=False)
    date_modified = models.DateTimeField(auto_now=True, blank=False)
    date_published = models.DateTimeField(auto_now=True)
    privacy_option = models.IntegerField(privacy_choices)

    class Meta:

        abstract = False
        ordering = ['title', 'description']

    def __unicode__(self):
        return self.description


class Album(models.Model):

    user = models.ForeignKey(User)
    title = models.CharField(max_length=127)
    description = models.CharField(max_length=127)
    cover_photo = models.ForeignKey(Photo)
    photos = models.ManyToManyField(Photo)
    privacy_option = models.IntegerField(choices=(('private', 0), ('shared', 1), ('public', 2)))

    class Meta:

        abstract = False
        ordering = ['title', 'description']

    def __unicode__(self):
        return self.description

class ImagrUser(models.Model):

    # username =
    # email =
    date_joined = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField()

    def __unicode__(self):
        return