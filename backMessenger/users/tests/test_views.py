import json
from django.urls import reverse
from django.test import TestCase, Client
from users.models import User


class TestViews(TestCase):

    def setUp(self):
        #creating test user
        self.user = User.objects.create_user(
        username='testuser', email='test@mail.ru', password='top_secret_password')

        #creating client and logged with test user
        self.client = Client()
        self.client.login(username='testuser', password='top_secret_password')

        #reversing urls
        self.whoami_url = reverse('whoami')
        self.contacts_url = reverse('contacts')


    def test_whoami_GET(self):
        response = self.client.get(self.whoami_url)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.user.id, json.loads(response.json())['user_id'])


    def test_getprofile_GET(self):
        profile_url = reverse('profile', args=[self.user.username])

        response = self.client.get(profile_url)
        self.assertEquals(len(json.loads(response.json())), 1)
        self.assertEquals(json.loads(response.json())['users'][0]['id'], self.user.id)

    def test_get_chat_list_GET(self):
        response = self.client.get(self.contacts_url)
        self.assertEquals(len(json.loads(response.json())), 0)

