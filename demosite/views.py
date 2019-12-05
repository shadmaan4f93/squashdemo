from django.http import HttpResponse


def index(request):
    return HttpResponse("My squash deployment demo is working!")