from django.urls import path, include
from chats.views import postChat, getChat, postMessage
urlpatterns = [
    #path('index/', index, name='index'),
    path('create_chat/', postChat, name='send_message'),
    path('get_chat/<int: chat_id>', getChat, name='index'),
    path('send_message/<int: chat_id>', postMessage, name='index'),
]