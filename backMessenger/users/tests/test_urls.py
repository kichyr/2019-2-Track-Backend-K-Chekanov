from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import get_chat_list

class TestUrls(SimpleTestCase):

    def test_contacts_list_urls_resolved(self):
        url = reverse('contacts')
        self.assertEquals(resolve(url).func, get_chat_list)