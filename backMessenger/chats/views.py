from django.http import JsonResponse, HttpResponseNotAllowed
from chats.models import Chat
from users.models import User
from users.models import Member
from django.views.decorators.csrf import csrf_exempt
from chats.models import Message
import datetime
from django.views.decorators.http import require_http_methods
from .forms import PostNewChatForm
import json
from django import forms

#------------------------------------
@csrf_exempt
@require_http_methods(["GET"])
def get_chat(request, chat_id):
    json_data = json.loads(request.body)
    login = json_data['login']
    #validation
    if len(
        Member.objects.filter(chat_id=chat_id).select_related(
        'user').filter(user__login=login)
    ) == 0:
        return JsonResponse({'errors': 'bad data'}, status=400)
    #
    return JsonResponse(
        json.dumps(get_chat_messages(chat_id, login)),
        status=200, safe=False)
    

def get_chat_messages(chat_id, user_login):
    """
    returns all messages in chat given by chat_id
    &
    update last_read_message_id in Member table for user with user_login
    """
    messages = Message.objects.filter(chat_id=chat_id).order_by(
        '-added_at').select_related('users').values(
            'id', 'users_id', 'users__avatar', 'added_at', 'content')
    
    #last_read_message_id in Member table
    if len(messages) > 0:
        Member.objects.filter(
            user_id=messages[0]['users_id'],
            chat_id=chat_id 
        )[0].last_read_message_id = messages[0]['id']

    for m in messages:
        m['added_at'] = m['added_at'].strftime("%d-%b-%Y (%H:%M:%S.%f)")

    return {
        'chat_id': chat_id,
        'topic': Chat.objects.filter(pk=chat_id).values('topic')[0]['topic'],
        'messages': [m for m in messages]
    }

#------------------------------------
@csrf_exempt
@require_http_methods(["POST"])
def post_message(request):
    form = PostMessageForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({}, status=200)
    return JsonResponse({'errors': form.errors}, status=400)


class PostMessageForm(forms.Form):
    content = forms.CharField(required=True)
    user_id = forms.IntegerField(required=True)
    chat_id = forms.IntegerField(required=True)
    
    def clean_text(self):
        user_id = self.cleaned_data['user_id']
        chat_id = self.cleaned_data['chat_id']
        if len(Member.objects.filter(
            user_id=user_id,
            chat_id=chat_id
        )) == 0:
            return 'wrong chat_id/user_id'
        return self.changed_data['user_id', 'chat_id']
    
    def save(self):
        Message.objects.create(
        chat_id=self.cleaned_data['chat_id'],
        users_id=self.cleaned_data['user_id'],
        content=self.cleaned_data['content'],
        added_at=datetime.datetime.now()
        )

#------------------------------------
@csrf_exempt
@require_http_methods(["POST"])
def post_chat(request):
    json_data = json.loads(request.body)
    topic = json_data['topic']
    users_logins = json_data['users_logins']
    create_new_chat(topic, users_logins)
    return JsonResponse({}, status=200)

def create_new_chat(topic, users_logins):
    """
    create new chat with topic
    attach to this chat list of users given by users_logins
    """
    group_chat_flag = False
    if len(users_logins) > 2:
        group_chat_flag = True

    chat = Chat.objects.create(topic=topic, is_group_chat=group_chat_flag)
    chat.save()
    for user_login in users_logins:
        user = User.objects.filter(login=user_login)[0]
        Member.objects.create(chat=chat, user=user).save()

