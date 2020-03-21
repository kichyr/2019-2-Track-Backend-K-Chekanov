from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseForbidden
from chats.models import Chat
from users.models import User
from users.models import Member
from django.views.decorators.csrf import csrf_exempt
from chats.models import Message
import datetime
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
import json
from django import forms
from chats.serializer import ChatSerializer


def check_permission(request, user_id):
    if request.user.id in user_id:
        return True
    return False

@login_required
@csrf_exempt
@require_http_methods(["GET"])
def get_chat(request, chat_id):

    #validation
    if len(
        Member.objects.filter(chat_id=chat_id).select_related(
        'user').filter(user__id=request.user.id)
    ) == 0:
        return JsonResponse({'errors': 'required authentication or'}, status=403)

    if len(Chat.objects.filter(id=chat_id)) == 0:
        return JsonResponse({'errors': 'chat does not exist'}, status=400)
    #
    return JsonResponse(
        json.dumps(get_chat_messages(chat_id, request.user.id)),
        status=200, safe=False)


def get_chat_messages(chat_id, user_id):
    """
    returns all messages in chat given by chat_id
    &
    update last_read_message_id in Member table for user with user_id
    """
    messages = Message.objects.filter(chat_id=chat_id).order_by(
        '-added_at').select_related('users').values(
            'id', 'users_id', 'users__avatar', 'added_at', 'content')

    # last_read_message_id in Member table
    if len(messages) > 0:
        Member.objects.filter(
            user_id=user_id,
            chat_id=chat_id 
        )[0].last_read_message_id = messages[0]['id']

    for m in messages:
        m['added_at'] = m['added_at'].strftime("%d-%b-%Y (%H:%M:%S.%f)")

    return {
        'chat_id': chat_id,
        'topic': Chat.objects.filter(pk=chat_id).values('topic')[0]['topic'],
        'messages': [m for m in messages]
    }


@login_required
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
        user_id = self.cleaned_data['user_id']
        chat_id = self.cleaned_data['chat_id']
        new_message = Message(
        chat_id=self.cleaned_data['chat_id'],
        users_id=self.cleaned_data['user_id'],
        content=self.cleaned_data['content'],
        added_at=datetime.datetime.now()
        )

        Member.objects.filter(
            user_id=user_id,
            chat_id=chat_id
        )[0].last_read_message = new_message.id
        new_message.save()

#------------------------------------
@login_required
@csrf_exempt
@require_http_methods(["POST"])
def post_chat(request):
    json_data = json.loads(request.body)
    topic = json_data['topic']
    users_ids = json_data['users_ids']
    create_new_chat(topic, users_ids)
    return JsonResponse({}, status=200)

def create_new_chat(topic, users_ids):
    """
    create new chat with topic
    attach to this chat list of users given by users_ids
    """
    group_chat_flag = False
    if len(users_ids) > 2:
        group_chat_flag = True

    chat = Chat.objects.create(topic=topic, is_group_chat=group_chat_flag)
    chat.save()
    for user_id in users_ids:
        user = User.objects.filter(id=user_id)[0]
        Member.objects.create(chat=chat, user=user).save()


@login_required
@csrf_exempt
@require_http_methods(["GET"])
def get_chat_serializer(request, chat_id):
    # validation
    if len(
        Member.objects.filter(chat_id=chat_id).select_related(
            'user').filter(user__id=request.user.id)
    ) == 0:
        return JsonResponse(
            {'errors': 'required authentication or'}, status=403)

    if len(Chat.objects.filter(id=chat_id)) == 0:
        return JsonResponse({'errors': 'chat does not exist'}, status=400)

    # getting last message for specific chat
    last_message = Message.objects.filter(chat_id=chat_id).order_by(
        '-added_at')[:1]

    # update last_read message in Member
    if len(last_message) > 0:
        Member.objects.filter(
            user_id=request.user.id,
            chat_id=chat_id
        )[0].last_read_message_id = last_message[0]['id']

    # after all validations and updates return serialized chat
    return JsonResponse(
        json.dumps(ChatSerializer(Chat.objects.get(pk=chat_id)).data),
        status=200, safe=False)


"""
@csrf_exempt
@require_http_methods(["POST"])
def upload_file(request):
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        handle_uploaded_file(request.FILES['file'])
        return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField() 
"""
