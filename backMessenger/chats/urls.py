from django.urls import path, include
from chats.views import index
urlpatterns = [
    path('index/', index, name='index')
]