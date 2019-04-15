from django.contrib.auth.models import User
from django.test import TestCase,Client
from apex.apps.services.forms import *

class TestSignup(TestCase):

	#Everything Valid
    def test_1(self):
        form = RegistrationForm(data={'username': "user",'email': "user@mp.com",'password1': "swapnild",'password2': "swapnild"})
        self.assertTrue(form.is_valid())

    #Remove @ from email
    def test_2(self):
        form = RegistrationForm(data={'username': "user",'email': "usermp.com",'password1': "swapnild",'password2': "swapnild"})
        self.assertTrue(not form.is_valid())

    #Blank username
    def test_3(self):
        form = RegistrationForm(data={'username': "",'email': "user@mp.com",'password1': "swapnild",'password2': "swapnild"})
        self.assertTrue(not form.is_valid())

    #Blank email
    def test_4(self):
        form = RegistrationForm(data={'username': "user",'email': "",'password1': "swapnild",'password2': "swapnild"})
        self.assertTrue(not form.is_valid())

    #Blank password1
    def test_5(self):
        form = RegistrationForm(data={'username': "user",'email': "user@mp.com",'password1': "",'password2': "swapnild"})
        self.assertTrue(not form.is_valid())

    #Blank password2
    def test_6(self):
        form = RegistrationForm(data={'username': "user",'email': "user@mp.com",'password1': "",'password2': "swapnild"})
        self.assertTrue(not form.is_valid())

    #Different password1 and password2
    def test_7(self):
        form = RegistrationForm(data={'username': "user",'email': "user@mp.com",'password1': "swapnild1",'password2': "swapnild"})
        self.assertTrue(not form.is_valid())

    

    