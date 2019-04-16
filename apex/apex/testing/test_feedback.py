from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.test import TestCase,Client
from apex.apps.services.forms import FeedbackForm
import pytest

class TestFeedback(TestCase):

    #Correct Feedback
    def test_1(self):
        form = FeedbackForm(data={'name': "Swapnil",'email': "sdhimmar006@gmail.com",'subject': "time pass",'message': "ihsif"})
        assert form.is_valid()

    #Blank username
    def test_2(self):
        form = FeedbackForm(data={'name': "",'email': "sdhimmar006@gmail.com",'subject': "time pass",'message': "ihsif"})
        assert not form.is_valid()

    #Blank email
    def test_3(self):
        form = FeedbackForm(data={'name': "Swapnil",'email': "",'subject': "time pass",'message': "ihsif"})
        assert not form.is_valid()

    #Blank subject
    def test_4(self):
        form = FeedbackForm(data={'name': "Swapnil",'email': "sdhimmar006@gmail.com",'subject': "",'message': "ihsif"})
        assert not form.is_valid()

    #Blank subject
    def test_5(self):
        form = FeedbackForm(data={'name': "Swapnil",'email': "sdhimmar006@gmail.com",'subject': "time pass",'message': ""})
        assert not form.is_valid()

    #Email missing @
    def test_6(self):
        form = FeedbackForm(data={'name': "Swapnil",'email': "sdhimmar006gmail.com",'subject': "time pass",'message': "ihsif"})
        assert not form.is_valid()

    #Email missing .com
    def test_7(self):
        form = FeedbackForm(data={'name': "Swapnil",'email': "sdhimmar006@gmail",'subject': "time pass",'message': "ihsif"})
        assert not form.is_valid()



