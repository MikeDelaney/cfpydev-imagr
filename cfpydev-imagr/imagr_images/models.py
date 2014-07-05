from django.db import models
from django.contrib.auth.models import User


class Photo(models.Model):

    image = models.ImageField(upload_to='photos/')
    user = models.ForeignKey(User) # we can also do user = models.ForeignKey("django.contrib.auth.models.User")
    title = models.CharField(max_length=127)
    description = models.CharField(max_length=127)
    date_uploaded = models.DateTimeField(auto_now_add=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True)
    date_published = models.DateTimeField(auto_now=True)
    published = models.IntegerField(choices=(('private', 0), ('shared', 1), ('public', 2)))

    class Meta:
        title = 'title'
        description = 'description'

    def __unicode__(self):
        return self.description

class Album(models.Model):

    user = models.ForeignKey(User)
    description = models.CharField(max_length=127)
    cover_photo = models.ForeignKey(Photo)
    photos = models.ManyToManyField(Photo)

    class Meta:
        title = 'title'
        description = 'description'

    def __unicode__(self):
        return self.description

class ImagrUser(models.Model):

    user_follow = models.ManyToManyField(User)
    date_joined = models.DateTimeField(auto_now_add=True)
    active =

    def __unicode__(self):
        return