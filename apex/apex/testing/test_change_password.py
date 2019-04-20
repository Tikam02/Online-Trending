from django.contrib.auth.models import User,AnonymousUser
from django.test import TestCase,Client
from django.contrib.auth.forms import PasswordChangeForm

class TestChangePassword(TestCase):
	
	def setUp(self):
		User.objects.create_user(username="swapnil",password="efwgegweh")

	#Correct Credentials
	def test_1(self):
		user = User.objects.get(username="swapnil")
		form = PasswordChangeForm(user=user,data={'user': "user",'old_password': "efwgegweh",
			'new_password1': "ojgihwneffq",'new_password2': "ojgihwneffq"})
		assert form.is_valid()

	#Entered different new password
	def test_2(self):
		user = User.objects.get(username="swapnil")
		form = PasswordChangeForm(user=user,data={'user': "user",'old_password': "efwgegweh",
			'new_password1': "ojgihwneffq",'new_password2': "ojgihwneff"})
		assert not form.is_valid()

	#Blank old_password
	def test_3(self):
		user = User.objects.get(username="swapnil")
		form = PasswordChangeForm(user=user,data={'user': "user",'old_password': "",
			'new_password1': "ojgihwneffq",'new_password2': "ojgihwneffq"})
		assert not form.is_valid()

	#Blank new_password1
	def test_4(self):
		user = User.objects.get(username="swapnil")
		form = PasswordChangeForm(user=user,data={'user': "user",'old_password': "efwgegweh",
			'new_password1': "",'new_password2': "ojgihwneffq"})
		assert not form.is_valid()

	#Blank new_password2
	def test_5(self):
		user = User.objects.get(username="swapnil")
		form = PasswordChangeForm(user=user,data={'user': "user",'old_password': "efwgegweh",
			'new_password1': "ojgihwneffq",'new_password2': ""})
		assert not form.is_valid()