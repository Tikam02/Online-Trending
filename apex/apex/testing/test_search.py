from django.contrib.auth.models import User
from django.test import TestCase,Client
from apex.apps.services.models import *
import pytest
from django.urls import reverse,resolve
from apex.apps.services.views import queryLookup

class TestSearch(TestCase):

	#add Bookmark
	@pytest.mark.django_db
	def test_search(self):
		response = self.client.get(reverse('search'),{'q': "Billy"})
		assert response is not None
		
	def test_searchquery(self):
		response=queryLookup('Billy')
		assert response.count()==1


