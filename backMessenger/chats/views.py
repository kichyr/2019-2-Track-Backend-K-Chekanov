from django.http import JsonResponse, Http404
# Create your views here

def postChat(request):
    if request.method == 'POST':
        pass
    else:
        raise Http404
    return JsonResponse({},status=200)
def getChat(request):
    if request.method == 'POST':
        pass
    else:
        raise Http404
    return JsonResponse({})

def postMessage(request, chat_id):
    if request.method == 'POST':
        pass
    else:
        raise Http404
    return JsonResponse({},status=200)
