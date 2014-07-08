from django.db import models
from django.contrib.auth.models import User, AbstractUser, UserManager
from imagr_site import settings

class Photo(models.Model):

    privacy_choices=(('private', 0), ('shared', 1), ('public', 2))
    image_upload_folder = '/Users/eyuelabebe/Desktop/projects/django-imagr/cfpydev-imagr/imagr_images'

    FOLLOWING_BITS = {
    'user_one': 1,
    'user_two': 2
    }

    FOLLOWER_STATUSES = (
        (0, u'not following'),
        (1, u'user_one following user_two'),
        (2, u'user_two following user_one'),
        (3, u'both following'),
    )

    FOLLOWER_SYMBOLS = {
    0: u' X ',
    1: u' +->',
    2: u'<-+ ',
    3: u'<+-+>',
    }

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

    owner = models.ForeignKey(User)
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


class ImagrUser(AbstractUser):
    relations = models.ManyToManyField('ImagrUser', through='Relationships', blank=True)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True

    def __unicode__(self):
        if self.first_name and self.last_name:
            name = self.first_name + self.last_name
        else:
            name = self.username

        return name


    def followers(self):
        pass
    def following(self):
        pass
    def follow(self):
        pass
    def unfollow(self, to_user):
        my_relation = _relationship_with(to_user)
        if not my_relation or (to_user not in self.following()):
            return
        for slot in ['user_one', 'user_two']:
            if getattr(my_relation, slot) != self:
                mask = FOLLOWING_BITS[slot]
                my_relation.follower_status &= mask
                my_relation.save()
                return

    def list_friends(self):
        pass
    def request_friendship(self):
        pass
    def end_friendship(self, to_user):
        my_relation = _relationship_with(to_user)
        if not my_relation or my_relation.friendship != 3:
            return
        my_relation.friendship = 3
        my_relation.save()

    def cancel_friendship_request(self, to_user):
        my_relation = _relationship_with(to_user)
        if not my_relation or my_relation == 0 or my_relation == 3:
            return
        for slot in ['user_one', 'user_two']:
            if getattr(my_relation, slot) != self:
                mask = FOLLOWING_BITS[slot]
                my_relation.friendship &= mask
                my_relation.save()
                return



    def accept_friendship_request(self):
        pass

    def _relationship_with(self, to_user):
        relationship = None
        try:
            relationship = Relationships.object.get(user_one=self, user_two=to_user)
        except Relationships.DoesNotExist:
            try:
                relationship = Relationships.objects.get(left=to_user, right=self)
            except Relationships.DoesNotExist:
                pass
        return relationship







class Relationships(models.Model):

    user_one = models.ForeignKey('ImagrUser', related_name='relationship_from')
    user_two = models.ForeignKey('ImagrUser', related_name='relationship_to')
    follower_status = models.IntegerField(choices = FOLLOWER_STATUSES )
    friendship = models.NullBooleanField(null=True, blank=True, default=None)


    def __unicode__(self):

        relationship_symbol = FOLLOWER_SYMBOLS.get(self.follower_status)
        if self.friendship:
            relationship_symbol += u"(F)"

        representation = u'{} {} {}'.format(unicode(self.user_one), relationship_symbol, unicode(self.user_two))

        return representation



