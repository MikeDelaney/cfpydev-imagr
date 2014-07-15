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


class StreamViewTests(TestCase):
    def test_setUp(self):
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




    user_list = [usr1, self.usr2, self.usr3, self.usr4]

    photo_list = ["{}_{}_{}".format("photo", item.username, i) for item in user_list for i in range(5)]
    base = datetime.datetime.today()
    date_list = [base - datetime.timedelta(days=x) for x in range(0, 20)]
    date_index = 0
    user_index = 0
    for item in photo_list:
        Photo(title=item,
                   description='test_description',
                   date_uploaded=date_list[date_index],
                   privacy_option=1,
                   owner=user_list[user_index]
                   )
        date_index +=1
        if not date_index % 5:
            user_index += 1

    import pdb;pdb.set_trace()
    print "here we are"
    # db den fotolar gercekten userlara yerlesmis mi bak
    print self.usr1, "--->>",type(self.usr1)
    print self.usr1.id

    usr1_photos = Photo.objects.filter(owner__exact=self.usr1.id)
    print len(usr1_photos)
    assert len(usr1_photos) == 5




    # eger hersey yolundaysa:
    # userlar arasinda iliskileri kurup test caseleri yazabilirsin
    # super!

















