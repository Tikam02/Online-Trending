from apex.apps.services.models import *
import pytest

@pytest.mark.django_db
class TestModels:

	def is_slug_unique(self):

		arr = []

		for service in Service.objects.all():
			arr.append(service)

		assert len(arr) == 7
