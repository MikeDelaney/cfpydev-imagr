from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_list_or_404
from imagr_images.models import Album, Photo
from imagr_user.models import ImagrUser


def home(request, user_id):
    template = loader.get_template('imagr_images/home.html')
    user = ImagrUser.objects.filter(id=user_id)
    album_list = get_list_or_404(Album, owner=user_id)
    context = RequestContext(request, {'user': user,
                                       'album_list': album_list},)
    return HttpResponse(template.render(context))
