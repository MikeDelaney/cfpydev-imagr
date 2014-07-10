from django.test import TestCase
from imagr_images.models import Photo, Album, ImagrUser, Relationships
from django.core.files import File
import datetime



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
            # cover_photo=img,
            privacy_option=1,
            )
        # self.assertEqual(album1.image,img)
        self.assertEqual(album1.title, "album1")
        self.assertEqual(album1.description, "test album 1")
        # self.assertEqual(album1.cover_photo, img)
        self.assertEqual(album1.privacy_option, 1)


class ImagrUser_Relations_Test(TestCase):

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


    def test_user_creation(self):
        self.assertEqual(self.usr2.first_name, 'Muazz')
        self.assertEqual(self.usr2.last_name, 'Mira')

    def test_followers_following(self):

        self.usr1.follow(self.usr2)

        self.assertEqual(list(self.usr1.following()), [self.usr2])
        self.assertEqual(list(self.usr2.following()), [])

        self.assertEqual(self.usr1.following()[0], self.usr2)
        self.assertEqual(self.usr2.followers()[0], self.usr1)
        self.assertEqual(self.usr1.relationship_from.get(user_two=self.usr2).follower_status, 1)
        self.assertEqual(self.usr2.relationship_to.get(user_two=self.usr2).follower_status, 1)

        self.usr1.unfollow(self.usr2)

        self.assertEqual(list(self.usr1.following()), [])
        self.assertEqual(list(self.usr2.followers()), [])
        self.assertEqual(self.usr1.relationship_from.get(user_one=self.usr1).follower_status, 0)
        self.assertEqual(self.usr2.relationship_to.get(user_two=self.usr2).follower_status, 0)


    def test_friendship(self):

        self.usr1.request_friendship(self.usr2)

        usr1_friendship_status = self.usr1.relationship_from.get(user_two=self.usr2).friendship
        usr2_friendship_status = self.usr2.relationship_to.get(user_one=self.usr1).friendship

        self.assertEqual(usr1_friendship_status, 1)
        self.assertEqual(usr2_friendship_status, 1)

        self.usr2.accept_friendship_request(self.usr1)

        usr1_friendship_status = self.usr1.relationship_from.get(user_two=self.usr2).friendship
        usr2_friendship_status = self.usr1.relationship_from.get(user_one=self.usr1).friendship

        self.assertEqual(usr1_friendship_status, 3)
        self.assertEqual(usr2_friendship_status, 3)

        self.usr1.end_friendship(self.usr2)

        usr1_friendship_status = self.usr1.relationship_from.get(user_two=self.usr2).friendship
        usr2_friendship_status = self.usr1.relationship_from.get(user_one=self.usr1).friendship

        self.assertEqual(usr1_friendship_status, 0)
        self.assertEqual(usr2_friendship_status, 0)


    def test_list_friendship(self):

        self.usr1.request_friendship(self.usr2)
        self.usr1.request_friendship(self.usr3)
        self.usr2.request_friendship(self.usr3)

        self.usr2.accept_friendship_request(self.usr1)
        self.usr3.accept_friendship_request(self.usr1)
        self.usr3.accept_friendship_request(self.usr2)

        usr1_list_friends = self.usr1.list_friends()
        usr2_list_friends = self.usr2.list_friends()
        usr3_list_friends = self.usr3.list_friends()

        self.assertEqual(list(usr1_list_friends), [self.usr2, self.usr3])
        self.assertEqual(list(usr2_list_friends), [self.usr1, self.usr3])
        self.assertEqual(list(usr3_list_friends), [self.usr1, self.usr2])
