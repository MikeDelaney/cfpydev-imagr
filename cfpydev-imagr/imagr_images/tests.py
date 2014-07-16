from django.test import TestCase
from imagr_images.models import Photo, Album, ImagrUser, Relationships
<<<<<<< HEAD
from imagr_images.views import albumView, photoView
=======
from imagr_images.views import streamView
>>>>>>> f3bc87f4b20f6b1c319e36160a82eec2cf40e6e4
import datetime
from django.test.client import RequestFactory
from django.core.files import File
from django.core.urlresolvers import reverse
from django.test.client import Client, RequestFactory
import os


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


class test_albumView(TestCase):

    def setUp(self):
        self.usr1 = ImagrUser(first_name='Eyuel', last_name='Abebe', username='Eyuel')
        self.usr1.save()

        test_image_path = os.path.dirname(__file__) + '/test_files/ocean.jpg'
        image = File(open(test_image_path, 'rb'))
        self.photo = Photo.objects.create(owner=self.usr1,
                                          image=image,
                                          title='ocean',
                                          description='Test pic',
                                          privacy_option=2)

        self.album = Album.objects.create(owner=self.usr1,
                                          title="ocean",
                                          description='Test album',
                                          privacy_option=2)
        self.album.photos = [self.photo]


    def test_albumView(self):
        request = self.factory.get(reverse('home'))
        request.user = self.usr1
        response = albumView(request, 1)
        self.assertEqual(response.status_code, 200)

        content = response.content
        # import pdb;pdb.set_trace()
        title_test = self.album.photos in content
        self.assertEqual(title_test, True)


class test_photoView(TestCase):

    def setUp(self):
        self.usr1 = ImagrUser(first_name='Eyuel', last_name='Abebe', username='Eyuel')
        self.usr1.save()

        test_image_path = os.path.dirname(__file__) + '/test_files/ocean.jpg'
        image = File(open(test_image_path, 'rb'))
        self.photo = Photo.objects.create(owner=self.usr1,
                                          image=image,
                                          title='ocean',
                                          description='Test pic',
                                          privacy_option=2)

        self.album = Album.objects.create(owner=self.usr1,
                                          title="ocean",
                                          description='Test album',
                                          privacy_option=2)
        self.album.photos = [self.photo]

        self.factory = RequestFactory()

    def tearDown(self):
        self.usr1.delete()
        self.photo.delete()
        self.album.delete()

    def test_albumView(self):
        request = self.factory.get(reverse('home'))
        request.user = self.usr1
        response = photoView(request, 1)
        self.assertEqual(response.status_code, 200)

        content = response.content
        # import pdb;pdb.set_trace()
        title_test = self.photo.title in content
        description_test = self.photo.description in content

        self.assertEqual(title_test, True)
        self.assertEqual(description_test, True)
