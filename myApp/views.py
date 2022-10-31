import imp
from django.shortcuts import render
from django.http import HttpResponse
from .tasks import func

# Create your views here.
def index(request):
    func.delay()
    return HttpResponse("Done")
    