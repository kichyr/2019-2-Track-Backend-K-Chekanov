from rest_framework import serializers
from chats.models import Message, Chat


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'topic']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        messages = Message.objects.filter(chat_id=instance['id']).order_by(
            '-added_at').select_related('users').values(
            'id', 'users_id', 'users__avatar', 'added_at', 'content')
        ret['messages'] = messages
        return ret


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'users_id', 'users__avatar', 'added_at', 'content']
