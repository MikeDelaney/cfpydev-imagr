from django.test import TestCase
from imagr_images.models import Photo, Album, ImagrUser, Relationships
from django.core.files import File
import datetime
from django.db.models import Q

# Create your tests here.


class PhotoTests(TestCase):

    def test_photo_creation(self):
        img = File(open('/Users/eyuelabebe/Desktop/projects/Network_tools2/root/static/images/java.jpg'))
        photo1 = Photo(image=img, title='test_title', description='test_description', date_uploaded= datetime.datetime.now(), privacy_option = 1)

        self.assertEqual(photo1.image, img)
        self.assertEqual(photo1.title, 'test_title')
        self.assertEqual(photo1.description, 'test_description')
        self.assertEqual(photo1.privacy_option, 1)
        # self.assertEqual(photo1.date_uploaded, datetime.datetime.now())

class AlbumTests(TestCase):
    def test_album_creation(self):
        img = File(open('/Users/eyuelabebe/Desktop/projects/Network_tools2/root/static/images/java.jpg'))
        album1 = Album(
            title="album1",
            description="test album 1",
            cover_photo=img,
            privacy_option=1,
            )
        self.assertEqual(album1.image,img)
        self.assertEqual(album1.title, "album1")
        self.assertEqual(album1.description, "test album 1")
        self.assertEqual(album1.cover_photo, img)
        self.assertEqual(album1.privacy_option, 1)


class ImagrUser_Relations_Test(TestCase):
    def test_user_creation(self):
        usr1 = ImagrUser(first_name='Eyuel', last_name='Abebe')

        self.assertEqual(usr1.first_name, 'Eyuel')
        self.assertEqual(usr1.last_name, 'Abebe')

    def test_followers_following(self):
        usr1 = ImagrUser(first_name='Eyuel', last_name='Abebe')
        usr2 = ImagrUser(first_name='Muazz', last_name='Mira')

        usr1_following = usr1.following()
        usr2_following = usr2.following()

        self.assertEqual(usr1_following, [])
        self.assertEqual(usr2_following, [])

        usr1.save()
        usr2.save()

        usr1.follow(usr2)

        self.assertEqual(usr1.following()[0], usr2)
        self.assertEqual(usr2.followers()[0], usr1)

        usr1.unfollow(usr2)

        self.assertEqual(usr1.following(), [])
        self.assertEqual(usr2.followers(), [])






