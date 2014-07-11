from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from imagr_images.models import Album, Photo
from imagr_user.models import ImagrUser


def home(request):
    template = loader.get_template('imagr_images/home.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))


