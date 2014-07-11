from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from imagr_images.models import Album, Photo, ImagrUser, Relationships

# Create your views here.
def albumView(request, album_id):
    # p = get_object_or_404(Album, pk=album_id)
    try:
        return render(request, 'imagr_images/albums.html')
    except (KeyError, NotImplementedError):
        return render(request, 'imagr_images/albums.html',{
            'error_message': 'Album was not selected'
        })