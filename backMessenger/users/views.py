from django.http import JsonResponse, HttpResponseNotAllowed
from users.models import User
from users.models import Member
from django.db.models import Q
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

@csrf_exempt
@require_http_methods(["GET"])
def get_chat_list(request, login):
    return JsonResponse(
        {"chats": json.dumps(get_chat_list_Impl(login))},
        status=200, safe=False)

@csrf_exempt
@require_http_methods(["GET"])
def get_profile(request, search_string):
    return JsonResponse(
        json.dumps(get_profile_Impl(search_string)),
        status=200, safe=False)


def get_profile_Impl(search_string):
    """return list of users that name/login/surname include search_string"""
    users = User.objects.filter(
        Q(login__contains=search_string) |
        Q(first_name__contains=search_string) |
        Q(last_name__contains=search_string)).values('login')
    return {'users': [user for user in users]}


def get_chat_list_Impl(login):
    """return list of chats belongs to user with sended login"""
    chat_list = Member.objects.select_related(
        'user').filter(user__login=login).select_related(
            'chat').values('chat_id', 'chat__topic', 'chat__last_message')
    return [chat for chat in chat_list]
