from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def homep(request):
    return HttpResponse("homep is succeed") 