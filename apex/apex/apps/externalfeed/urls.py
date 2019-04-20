from django.conf.urls import url

from apex.apps.externalfeed.views import Index, List, Entry

urlpatterns = [
    url(r'^$', Index.as_view(), name='externalfeed-index'),
    url(r'^list/$', List.as_view(), name='externalfeed-list'),
    url(r'^(?P<path>.*)$', Entry.as_view(), name='externalfeed-entry'),
    ]
