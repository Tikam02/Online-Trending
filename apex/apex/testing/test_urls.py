from django.urls import reverse,resolve
from apex.apps.services.models import *
import pytest

class TestUrls:
    
    def test_login_url(self):
        path = reverse('login')
        assert resolve(path).view_name == 'login'

    def test_logout_url(self):
        path = reverse('logout')
        assert resolve(path).view_name == 'logout'

    def test_front_page(self):
        path = reverse('front_page')
        assert resolve(path).view_name == 'front_page'

    def test_signup_page(self):
        path = reverse('signup')
        assert resolve(path).view_name == 'signup'