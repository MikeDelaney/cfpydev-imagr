from django.test import TestCase
from imagr_images.models import Photo, Album, ImagrUser, Relationships
import datetime


class PhotoTests(TestCase):

    def test_photo_creation(self):
        photo1 = Photo(title='test_title',
                       description='test_description',
                       date_uploaded=datetime.datetime.now(),
                       privacy_option=1)

        self.assertEqual(photo1.title, 'test_title')
        self.assertEqual(photo1.description, 'test_description')
        self.assertEqual(photo1.privacy_option, 1)

class AlbumTests(TestCase):
    def test_album_creation(self):
        album1 = Album(title="album1",
                       description="test album 1",
                       privacy_option=1,
                      )
        self.assertEqual(album1.title, "album1")
        self.assertEqual(album1.description, "test album 1")
        self.assertEqual(album1.privacy_option, 1)

class test_photoView(TestCase):
    
    def setUp(self):

        self.usr1 = ImagrUser(first_name='Eyuel', last_name='Abebe', username='Eyuel')
        self.usr2 = ImagrUser(first_name='Muazz', last_name='Mira', username='Muazz')
        self.usr3 = ImagrUser(first_name='Mike', last_name='Delany', username='Mike')

        self.usr1.save()
        self.usr2.save()
        self.usr3.save()

    def tearDown(self):

        self.usr1.delete()
        self.usr2.delete()
        self.usr3.delete()

