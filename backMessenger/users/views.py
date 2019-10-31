from django.shortcuts import render
from django.http import JsonResponse, Http404
# Create your views here.

def getContacts(request):
    if request.method == 'GET':
        pass
    else:
        raise Http404
    return JsonResponse({'test': 'test'})

def getProfile(request, login):
    if request.method == 'GET':
        pass
    else:
        raise Http404
    return JsonResponse({'test': 'test'})