from django.urls import reverse, resolve
from users.views import get_chat_list, get_profile, whoami
from django.test import SimpleTestCase


class TestUrls(SimpleTestCase):

    def test_contacts_list_urls_resolved(self):
        url = reverse('contacts')
        self.assertEquals(resolve(url).func, get_chat_list)

    def test_profile_urls_resolved(self):
        url = reverse('profile', args=['fake-query'])
        self.assertEquals(resolve(url).func, get_profile)

    def test_whoami_urls_resolved(self):
        url = reverse('whoami')
        self.assertEquals(resolve(url).func, whoami)
