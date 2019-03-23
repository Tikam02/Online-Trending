def changebm(self,request,checked,story):
	
	if checked=="checked":
		user.bookmarks.add(story)
	elif story in user.bookmarks:
		user.bookmarks.remove(story)

	return
