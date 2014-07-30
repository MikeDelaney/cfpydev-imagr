from django.template import RequestContext
from django.shortcuts import get_list_or_404, render_to_response, get_object_or_404
from imagr_images.models import Album
from imagr_user.models import ImagrUser
from django.core.exceptions import ObjectDoesNotExist


def home(request):

    user_ = get_object_or_404(ImagrUser, pk=request.user.id)
    #album_list = get_list_or_404(Album, owner=request.user.id)
    try :
        album_list = Album.objects.get(owner=request.user.id)
    except ObjectDoesNotExist:
        album_list=[]
    context = RequestContext(request, {'ImagrUser': user_,
                                       'album_list': album_list},)

    return render_to_response('imagr_images/home.html',
                              context_instance=context)


