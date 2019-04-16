from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.test import TestCase,Client
from apex.apps.services.forms import *

class TestLogin(TestCase):
	
    def setUp(self):
    	User.objects.create_user(username="swapnil",password="efwgegweh")

    #Correct credentials
    def test_1(self):
    	form = AuthenticationForm(data={'username': "swapnil",'password': "efwgegweh"})
    	assert form.is_valid()

    #Wrong Password
    def test_2(self):
    	form = AuthenticationForm(data={'username': "swapnil",'password': "efwgegwe"})
    	assert not form.is_valid()

    #Wrong Username
    def test_3(self):
    	form = AuthenticationForm(data={'username': "swapni",'password': "efwgegweh"})
    	assert not form.is_valid()

    #Blank password
    def test_4(self):
    	form = AuthenticationForm(data={'username': "swapni",'password': ""})
    	assert not form.is_valid()