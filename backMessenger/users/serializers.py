from rest_framework import serializers
from chats.models import Chat
from users.models import User


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'first_name']
