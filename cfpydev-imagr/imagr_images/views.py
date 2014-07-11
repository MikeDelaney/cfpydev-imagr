
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from imagr_images.models import Album, Photo, ImagrUser, Relationships


def home(request):
    template = loader.get_template('imagr_images/home.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def front(request):
    template = loader.get_template('imagr_images/front.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))


def albumView(request, album_id):
    # p = get_object_or_404(Album, pk=album_id)
    try:
        return render(request, 'imagr_images/albums.html')
    except (KeyError, NotImplementedError):
        return render(request, 'imagr_images/albums.html',{
            'error_message': 'Album was not selected'
        })
