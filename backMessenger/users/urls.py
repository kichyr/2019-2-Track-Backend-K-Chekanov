from django.urls import path, include
from users.views import getContacts, getProfile
urlpatterns = [
    path('contacts_list/', getContacts, name='contacts'),
    path('profile/<string: login>', getProfile, name='profile'),
]