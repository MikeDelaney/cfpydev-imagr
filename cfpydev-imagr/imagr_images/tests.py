from django.test import TestCase
from imagr_images.models import Photo, Album, ImagrUser, Relationships
import datetime
from django.test.client import Client
from django.core.files import File


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

class StreamViewTests(TestCase):
    def setUp(self):
        self.usr1 = ImagrUser(first_name='Eyuel', last_name='Abebe', username='Eyuel')
        self.usr2 = ImagrUser(first_name='Muazz', last_name='Mira', username='Muazz')
        self.usr3 = ImagrUser(first_name='Mike', last_name='Delany', username='Mike')
        self.usr4 = ImagrUser(first_name='Sean', last_name='SeanLast', username='Sean')
        self.usr5 = ImagrUser(first_name='John', last_name='Shiver', username='John')

        self.usr1.save()
        self.usr2.save()
        self.usr3.save()
        self.usr4.save()
        self.usr5.save()
        user_list = [ self.usr1, self.usr2, self.usr3, self.usr4]

        photo_list = ["{}_{}_{}".format("photo", item.username, i) for item in user_list for i in range(5)]
        base = datetime.datetime.today()
        date_list = [base - datetime.timedelta(days=x) for x in range(0, 20)]
        date_index = 0
        user_index = 0
        for item in photo_list:
            with open('/Users/muazzezmira/projects/django_imagr/cfpydev-imagr/cfpydev-imagr/imagr_images/static/front_img/7fTNh.jpg', 'r') as f:
                photo_file = File(f)
                photo = Photo()
                photo.image = photo_file
                photo.title = item
                photo.owner = user_list[user_index]
                photo.privacy_option = 2
                photo.date_uploaded=date_list[date_index]
                photo.save()
            date_index +=1
            if not date_index % 5:
                user_index += 1
            photo.save()

        self.usr1.request_friendship(self.usr2)
        self.usr2.accept_friendship_request(self.usr1)

        self.usr2.request_friendship(self.usr4)
        self.usr4.accept_friendship_request(self.usr2)

        self.usr1.follow(self.usr3)
        self.usr4.follow(self.usr1)
        self.usr1.follow(self.usr5)
        self.usr5.follow(self.usr1)


    def tearDown(self):

        self.usr1.delete()
        self.usr2.delete()
        self.usr3.delete()
        self.usr4.delete()
        self.usr5.delete()


    def test_stream(self):
            # db den fotolar gercekten userlara yerlesmis mi bak
        usr1_photos = Photo.objects.filter(owner__exact=self.usr1.id)
        usr2_photos = Photo.objects.filter(owner__exact=self.usr2.id)
        usr3_photos = Photo.objects.filter(owner__exact=self.usr3.id)
        usr4_photos = Photo.objects.filter(owner__exact=self.usr4.id)
        usr5_photos = Photo.objects.filter(owner__exact=self.usr5.id)
        assert len(usr1_photos) == 5
        assert len(usr2_photos) == 5
        assert len(usr3_photos) == 5
        assert len(usr4_photos) == 5
        assert len(usr5_photos) == 0

        c = Client()
        response = c.get('/stream/' + str(self.usr1.id) + '/')
        print response
        # self.assertEqual(response.status_code, 200)



        # eger hersey yolundaysa:
        # userlar arasinda iliskileri kurup test caseleri yazabilirsin
        # super!

















