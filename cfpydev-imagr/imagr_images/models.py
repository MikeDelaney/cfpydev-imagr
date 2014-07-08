from django.db import models
from django.contrib.auth.models import User, AbstractUser, UserManager
from imagr_site import settings
from django.db.models import Q

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

    FRIEND_STATUSES = (
        (0, u'not friends'),
        (1, u'user_one requesting user_two'),
        (2, u'user_two requesting user_one'),
        (3, u'friends'),
    )

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
    def unfollow(self):
        pass

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


    def end_friendship(self):
        pass

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
    follower_status = models.IntegerField(choices=FOLLOWER_STATUSES)
    friendship = models.IntegerField(choices=FRIEND_STATUSES)


    def __unicode__(self):

        relationship_symbol = FOLLOWER_SYMBOLS.get(self.follower_status)
        if self.friendship:
            relationship_symbol += u"(F)"

        representation = u'{} {} {}'.format(unicode(self.user_one), relationship_symbol, unicode(self.user_two))

        return representation



