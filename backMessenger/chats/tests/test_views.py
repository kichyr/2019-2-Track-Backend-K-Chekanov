import json
import factory
import datetime
from django.urls import reverse
from factory import fuzzy
from django.test import TestCase, Client
from chats.models import Message, Chat
from users.models import User, Member
from users.urls import *


class UserFactory(factory.Factory):
    class Meta:
        model = User
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    login = factory.fuzzy.FuzzyText(length=10)


class ChatFactory(factory.Factory):
    class Meta:
        model = Chat
    is_group_chat = False
    topic = factory.fuzzy.FuzzyText(length=5)


class MessageFactory(factory.Factory):

    class Meta:
        model = Message

    chat = ChatFactory()
    users = UserFactory()
    content = factory.fuzzy.FuzzyText(length=50)
    added_at = factory.fuzzy.FuzzyDateTime(
        datetime.datetime(2008, 1, 1, tzinfo=datetime.timezone.utc)
        )

class TestViews(TestCase):

    def setUp(self):
        #creating test user
        self.user = User.objects.create_user(
        username='testuser', email='test@mail.ru', password='top_secret_password')

        #creating client and logged with test user
        self.client = Client()
        self.client.login(username='testuser', password='top_secret_password')



    def test_get_chat(self):
        chat = ChatFactory()
        chat.save()
        Member(user=self.user, chat=chat).save()
        for i in range(30):
            MessageFactory(users=self.user, chat=chat).save()

        self.contacts_url = reverse('get_chat', args=[chat.id])


        response = self.client.get(self.contacts_url)
        self.assertEquals(response.status_code, 200)

        self.assertEquals(len(json.loads(response.json())['messages']), 30)