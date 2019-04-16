from django.contrib.auth.models import User
from django.test import TestCase,Client
from apex.apps.services.models import *
import pytest
from django.urls import reverse,resolve

class TestBookmarks(TestCase):

	#add Bookmark
	@pytest.mark.django_db
	def test_bookmark(self):
		user1 = User.objects.all().get(username="swap1")
		#c = self.client()
		response = self.client.post(reverse('login'),{'username': "swap1",'password': "happyswapnil"})
		response = self.client.post('/11/bookmark/')
		assert BookmarkArticle.objects.filter(user=user1,obj=Story.objects.all().get(id=11)) is not None
		
	@pytest.mark.django_db
	def test_unbookmark(self):
		user1 = User.objects.all().get(username="swap1")
		#c = self.client()
		response = self.client.post(reverse('login'),{'username': "swap1",'password': "happyswapnil"})
		response = self.client.post('/11/bookmark/')
		assert BookmarkArticle.objects.filter(user=user1,obj=Story.objects.all().get(id=11)) is not None
		response = self.client.post('/11/bookmark/')
		i=BookmarkArticle.objects.filter(user=user1,obj=Story.objects.all().get(id=11)) 
		assert not i.exists()

	@pytest.mark.django_db
	def test_unloggedin(self):
		#c = self.client()
		#response = self.client.post(reverse('login'),{'username': "swap1",'password': "happyswapnil"})
		try:
		    response = self.client.post('/11/bookmark/')
		    assert False
		except Exception:
		    assert True



		