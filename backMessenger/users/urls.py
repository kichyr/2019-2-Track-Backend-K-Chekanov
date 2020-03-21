from django.urls import path
from users.views import (
    get_chat_list, get_profile,
    whoami,
    get_chat_list_serializer,
    get_profile_serializer)

urlpatterns = [
    path('contacts_list/', get_chat_list, name='contacts'),

    path(
        'contacts_list/v2',
        get_chat_list_serializer,
        name='contacts_serializer'),  # serializer

    path(
        'profile/v2/<str:search_string>',
        get_profile_serializer,
        name='profile_serializer'),  # serializer

    path('profile/<str:search_string>', get_profile, name='profile'),

    path('whoami/', whoami, name='whoami'),
]
