from django.http import HttpResponse
from django.template import loader


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def login(request):
    template = loader.get_template('frontend/login.html')
    context = {}
    return HttpResponse(template.render(context, request))

def register(request):
    template = loader.get_template('frontend/register.html')
    context = {}
    return HttpResponse(template.render(context, request))

def scan(request):
    template = loader.get_template('frontend/scan.html')
    context = {}
    return HttpResponse(template.render(context, request))
