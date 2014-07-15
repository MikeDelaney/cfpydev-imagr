from django.template import RequestContext
from django.shortcuts import get_list_or_404, render_to_response
from imagr_images.models import Album
from imagr_user.models import ImagrUser


def home(request, user_id):
    user_ = ImagrUser.objects.get(pk=user_id)
    album_list = get_list_or_404(Album, owner=user_id)
    context = RequestContext(request, {'ImagrUser': user_,
                                       'album_list': album_list},)

    return render_to_response('imagr_images/home.html',
                              context_instance=context)


