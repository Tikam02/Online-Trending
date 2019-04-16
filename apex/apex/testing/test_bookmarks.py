from django.contrib.auth.models import User
from django.test import TestCase,Client
from apex.apps.services.models import *
import pytest

class TestBookmarks(TestCase):

	#add Bookmark
	@pytest.mark.django_db
	def test_1(self):
		user1 = Story.objects.all().count()
		# story = Story.objects.filter(id=4)
		# self.client.post('47/bookmark/',{'user': "user1"})
		assert user1 > 0