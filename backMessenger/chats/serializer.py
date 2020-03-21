from rest_framework import serializers

class ChatSerializer(serializers.Serializers):
    chat_id = serializers.IntegerField(read_only=True)
    topic = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=30)
    description = serializers.CharField()
    description_html = serializers.CharField(source='description', read_only=True)

    def transform_description_html(self, obj, value):
        from django.contrib.markup.templatetags.markup import markdown
        return markdown(value)

class MessageSerializer(serializers.Serializers):
