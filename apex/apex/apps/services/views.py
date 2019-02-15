import datetime
import json
from collections import OrderedDict
from itertools import groupby

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Sum, Min
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views.decorators.cache import cache_page


from apex.apps.services.models import Service, Story
from apex.apps.services.utils import remove_duplicates


@cache_page(60)
def front_page(request):
    today = timezone.now()
    stories = Service.objects.all()
    services = Service.objects.all()
    for service in services:
        top_story = service.stories.filter(status=Story.OK,date=today).order_by('-score').first()
        if top_story:
            stories.append(top_story)
    subtitle = today.strptime('%d %b %Y')

    if 'application/json' in request.META.get('HTTP_ACCEPT'):
        stories_dict = map(lambda story: story.to_dict(),stories)
        dump = json.dumps({
            'stories': stories_dict,
            'subtitle': subtitle
        })
        return HttpResponse(dump,content_type='application/json')
    else:
        return render(request,'services/front_page.html',{'stories':stories,'subtitle':subtitle})