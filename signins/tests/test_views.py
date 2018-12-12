from django.test import TestCase
from datetime import timedelta
from django.urls import reverse
from unittest.mock import patch
from ..views import GetHome, SignInUser


class TestGetHome(TestCase):
    @patch('signins.models.Student.signins_for_today')
    def test_home_shows_todays_sign_ins(self, _patch_signins_for_today):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.context['students'],
                         _patch_signins_for_today.return_value)
