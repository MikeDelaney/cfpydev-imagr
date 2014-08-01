from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from imagr_images.models import Album
from imagr_user.models import ImagrUser


@login_required(login_url='/accounts/login/')
def home(request):
    user_ = get_object_or_404(ImagrUser, pk=request.user.id)
    album_list = Album.objects.filter(owner=request.user.id)
    context = RequestContext(request, {'ImagrUser': user_,
                                       'album_list': album_list},)
    return render_to_response('imagr_images/home.html',
                              context_instance=context)
