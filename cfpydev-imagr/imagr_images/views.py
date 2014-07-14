from django.shortcuts import render_to_response
from django.shortcuts import get_list_or_404
from django.template import RequestContext
from imagr_images.models import Album, Photo, ImagrUser, Relationships


def get_photo_list(album_id):

    album = Album.objects.filter(id__exact=album_id)[0]
    return album.photos.all()


def get_photo(photo_id):
    return Photo.objects.filter(id__exact=photo_id)[0]


def albumView(request, album_id):
    photo_list = get_photo_list(album_id)
    return render_to_response('imagr_images/albumView.html',
                              context_instance=RequestContext(request,
                                                              {'photo_list': photo_list}))


def photoView(request, photo_id):
    photo = get_photo_list(photo_id)
    return render_to_response('imagr_images/photoView.html',
                              context_instance=RequestContext(request,
                                                              {'photo': photo}))