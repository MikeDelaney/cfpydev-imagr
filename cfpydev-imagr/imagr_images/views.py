from django.shortcuts import render_to_response
from django.template import RequestContext
from imagr_images.models import Album, Photo, ImagrUser, Relationships
from django.contrib.auth.decorators import login_required

def get_followings_friends (user_id):
    user = ImagrUser.objects.get(pk=user_id)
    user_list = []
    user_list.append(user)
    user_list += [item for item in user.following() if not item in user_list]
    user_list += [item for item in user.list_friends() if not item in user_list]
    return user_list

def get_photo_list(album_id):
    album = Album.objects.filter(id__exact=album_id)[0]
    return album.photos.all()

def get_users_photo_list(user_id):
    user_list = get_followings_friends(user_id)
    return Photo.objects.filter(owner__in=user_list).order_by('date_uploaded')


def get_photo(photo_id):
    return Photo.objects.filter(id__exact=photo_id)[0]


@login_required(login_url='/accounts/login/')
def albumView(request, album_id):
    photo_list = get_photo_list(album_id)
    return render_to_response('imagr_images/albumView.html',
                              context_instance=RequestContext(request,
                                                              {'photo_list': photo_list}))


@login_required(login_url='/accounts/login/')
def photoView(request, photo_id):
    photo = get_photo(photo_id)
    return render_to_response('imagr_images/photoView.html',
                              context_instance=RequestContext(request,
                                                              {'photo': photo}))


@login_required(login_url='/accounts/login/')
def streamView(request):
    photo_list = get_users_photo_list(request.user.id)
    for item in photo_list:
        print item
    return render_to_response('imagr_images/stream.html',
                            context_instance=RequestContext(request,
                                                            {'photo_list': photo_list}))



