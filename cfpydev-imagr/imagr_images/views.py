from django.shortcuts import get_object_or_404, render_to_response
from django.shortcuts import render, get_list_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from imagr_images.models import Album, Photo, ImagrUser, Relationships


def albumView(request, album_id):
    template = loader.get_template('imagr_images/albumView.html')
    return render_to_response('imagr_images/albumView.html',
                              context_instance=RequestContext(request))
