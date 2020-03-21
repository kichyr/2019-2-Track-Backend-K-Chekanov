from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class LoginTest(TestCase):

    def setUp(self):
        self.selenium = webdriver.Chrome()

    def tearDown(self):
        self.selenium.quit()

    def test_register(self):
        """ Open login page on localhost."""
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/')
        login_redirect_vk_butt = selenium.find_element_by_id('login_vk_link')
        login_redirect_vk_butt.click()
        time.sleep(2)
        assert "VK" in selenium.title
