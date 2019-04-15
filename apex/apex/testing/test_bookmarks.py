from django.contrib.auth.models import User
from django.test import TestCase,Client
from apex.apps.services.models import *

class TestBookmarks(TestCase):

	#add Bookmark
	def test_1(self):
		user1 = User.objects.all().count()
		# story = Story.objects.filter(id=4)
		# self.client.post('47/bookmark/',{'user': "user1"})
		assert user1 > 0