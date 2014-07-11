from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader

def front(request):
    template = loader.get_template('imagr_images/front.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))