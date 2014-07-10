from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader


def front(request):
    template = loader.get_template('imagr_images/front.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))


def home(request):
    template = loader.get_template('imagr_images/home.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))
