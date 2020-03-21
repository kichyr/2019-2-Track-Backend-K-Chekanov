from django.urls import path
from chats.views import post_chat, get_chat, post_message

urlpatterns = [
    # path('index/', index, name='index'),
    path('create_chat', post_chat, name='post_chat'),
    path('get_chat/<int:chat_id>', get_chat, name='get_chat'),
    path('get_chat_serializer/<int:chat_id>',
        get_chat, name='get_chat_serializer'),  # serializer
    path('send_message', post_message, name='post_message'),
    # path('read_message/<int:message_id>', )
]