from django.db import models
from django.contrib.auth.models import AbstractUser
from imagr_site import settings
from django.db.models import Q
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.core.files.images import get_image_dimensions
import os

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

FRIEND_STATUSES = (
    (0, u'not friends'),
    (1, u'user_one requesting user_two'),
    (2, u'user_two requesting user_one'),
    (3, u'friends'),
)

privacy_choices = (('private', 0), ('shared', 1), ('public', 2))

class Photo(models.Model):

    image_upload_folder = '/Users/eyuelabebe/Desktop/projects/django-imagr/cfpydev-imagr/imagr_images/upload_images'
    image = models.ImageField(upload_to=image_upload_folder)
    # image_size = os.path.getsize(image)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='photo_owner')
    title = models.CharField(max_length=127)
    description = models.CharField(max_length=127)
    date_uploaded = models.DateTimeField(auto_now_add=True, blank=False)
    date_modified = models.DateTimeField(auto_now=True, blank=False)
    date_published = models.DateTimeField(auto_now=True)
    privacy_option = models.IntegerField(privacy_choices)

    class Meta:

        # abstract = False
        ordering = ['title', 'description']

    def __unicode__(self):
        return self.description


class Album(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='Album_owner')
    title = models.CharField(max_length=127)
    description = models.CharField(max_length=127)
    cover_photo = models.ForeignKey(Photo, related_name='cover_photo')
    photos = models.ManyToManyField(Photo, related_name='album_photo')
    privacy_option = models.IntegerField(privacy_choices)


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
        # abstract = True

    def __unicode__(self):
        if self.first_name and self.last_name:
            # added a space for presentation
            name = self.first_name + ' ' + self.last_name
        else:
            name = self.username

        return name

    def followers(self):
        """Returns a sql query object for list of self's followers"""
        user_one_followers = (
            Q(relationship_from__user_two=self) & \
            Q(relationship_from__follower_status__in=[1, 3]))

        user_two_followers = (
            Q(relationship_to__user_one=self) & \
            Q(relationship_to__follower_status__in=[2, 3]))

        followers = ImagrUser.objects.filter(
            Q(user_one_followers | user_two_followers)
        )

        return followers

    def list_friends(self):
        friends = filter(
            (Q(relationship_from__user_one=self) &
             Q(relationship_from__friendship__exact=True)) |
            (Q(relationship_to__user_two=self) &
             Q(relationship_to__friendship__exact=True))
        )
        return friends

    def request_friendship(self, other):
        if other not in self.list_friends():
            rel = self._relationship_with(other)
            if rel is not None:
                for slot in ['user_one', 'user_two']:
                    if getattr(rel, slot) == self:
                        if rel.friendship not in (1, 2):
                            bitmask = FOLLOWING_BITS[slot]
                            rel.friendship = rel.friendship | bitmask
                            break
        rel.full_clean()
        rel.save()

    def accept_friendship_request(self, other):
        if other not in self.list_friends():
            rel = self._relationship_with(other)
            if rel is not None:
                rel.friendship = 3
            else:
                rel = Relationships(user_one=self,
                                    user_two=other,
                                    follower_status=0,
                                    friendship=3)

    def following(self):
        """Returns a sql query object for list of users self is following"""
        following_user_one = (
            Q(relationship_to__user_one=self) &
            Q(relationship_to__follower_status__in=[1, 3])
        )

        following_user_two = (
            Q(relationship_from__user_two=self) &
            Q(relationship_from__follower_status__in=[2, 3])
        )

        followers = ImagrUser.objects.filter(
            Q(following_user_one | following_user_two)
        )

        return followers

    def follow(self, a_user):
        """
        self follow other users.
        If a relationship does not exist between self and user, one is created.
        Relationship is validated before save. Calling code handles errors.
        """
        if a_user not in self.following():
            relationship = self._relationship_with(self, a_user)
            if relationship is not None:
                for slot in ['user_one', 'user_two']:
                    if getattr(relationship, slot) == self:
                        bitmask = FOLLOWING_BITS[slot]
                        relationship.follower_status = relationship.follower_status | bitmask
                        break
            else:
                relationship = Relationships(user_one=self, user_two=a_user, follower_status=1)
                relationship.full_clean()
                relationship.save()

    def unfollow(self, to_user):
        my_relation = self._relationship_with(to_user)
        if not my_relation or (to_user not in self.following()):
            return
        for slot in ['user_one', 'user_two']:
            if getattr(my_relation, slot) != self:
                mask = FOLLOWING_BITS[slot]
                my_relation.follower_status &= mask
                my_relation.save()
                return

    def end_friendship(self, to_user):
        my_relation = self._relationship_with(to_user)
        if not my_relation or my_relation.friendship != 3:
            return
        my_relation.friendship = 3
        my_relation.save()

    def cancel_friendship_request(self, to_user):
        my_relation = self._relationship_with(to_user)
        if not my_relation or my_relation == 0 or my_relation == 3:
            return
        for slot in ['user_one', 'user_two']:
            if getattr(my_relation, slot) != self:
                mask = FOLLOWING_BITS[slot]
                my_relation.friendship &= mask
                my_relation.save()
                return


    def _relationship_with(self, a_user):
        """Returns a relationship object(row from Relationships table) or none if there is no existing relationship."""
        relationship = None
        try:
            relationship = Relationships.object.get(user_one=self, user_two=a_user)
        except Relationships.DoesNotExist:
            try:
                relationship = Relationships.objects.get(left=a_user, right=self)
            except Relationships.DoesNotExist:
                pass
        return relationship



class Relationships(models.Model):

    user_one = models.ForeignKey('ImagrUser', related_name='relationship_from')
    user_two = models.ForeignKey('ImagrUser', related_name='relationship_to')
    follower_status = models.IntegerField(choices=FOLLOWER_STATUSES)
    friendship = models.IntegerField(choices=FRIEND_STATUSES)


    def __unicode__(self):

        relationship_symbol = FOLLOWER_SYMBOLS.get(self.follower_status)
        if self.friendship:
            relationship_symbol += u"(F)"

        representation = u'{} {} {}'.format(unicode(self.user_one), relationship_symbol, unicode(self.user_two))

        return representation



