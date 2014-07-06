from django.test import TestCase
from imagr_images.models import Photo, Album
from django.core.files import File
import datetime

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


