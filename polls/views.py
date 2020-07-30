from django.http import HttpResponse


def index(request):
    return HttpResponse("M Rijal Al Fariz")