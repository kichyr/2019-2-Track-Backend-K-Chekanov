from django.urls import path
from users.views import get_chat_list, get_profile, whoami
urlpatterns = [
    path('contacts_list/', get_chat_list, name='contacts'),
    path('profile/<str:search_string>', get_profile, name='profile'),
    path('whoami/', whoami, name='whoami'),
]
