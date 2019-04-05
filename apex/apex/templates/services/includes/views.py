from django.shortcuts import render

from apex.apps.services.models import BookmarkArticle

from django.contrib.auth.models import User

from apex.apps.services.models import BookmarkArticle,Service

from django.views import View

from django.contrib import auth

class BookmarksView(View):
	
	model = None

	def get(self,request):
		bookmarks = BookmarkArticle.objects.all()
		user = auth.get_user(request)
		service = Service.objects.all()
		context = {'user': user, 'bookmarks': bookmarks,'services': service}
		return render(request,"bookmarks.html",context)