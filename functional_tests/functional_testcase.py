from splinter import Browser
from django.test import TestCase


class FunctionalTestCase(TestCase):
    def setUp(self):
        super().setUp()
        self.browser = Browser('django')

    def tearDown(self):
        super().tearDown()
        self.browser.quit()