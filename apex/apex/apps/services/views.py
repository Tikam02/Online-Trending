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


def stories(request, service, queryset, subtitle):
    paginator = Paginator(queryset, 100)
    page = request.GET.get('page')
    try:
        stories = paginator.page(page)
    except PageNotAnInteger:
        stories = paginator.page(1)
    except EmptyPage:
        stories = paginator.page(paginator.num_pages)

    if stories.number > 1:
        start = (stories.number - 1) * 100 + 1
    else:
        start = 1

    if 'application/json' in request.META.get('HTTP_ACCEPT'):
        stories_dict = map(lambda story: story.to_dict(), stories)
        dump = json.dumps({
            'service': service.to_dict(),
            'stories': stories_dict,
            'subtitle': subtitle
        })
        return HttpResponse(dump, content_type='application/json')
    else:
        return render(request, 'services/stories.html', {
            'service': service,
            'stories': stories,
            'subtitle': subtitle,
            'start': start
        })


@cache_page(60)
def front_page(request):
    today = timezone.now()
    stories = list()
    services = Service.objects.all()
    for service in services:
        top_story = service.stories.filter(status=Story.OK, date=today).order_by('-score').first()
        if top_story:
            stories.append(top_story)
    subtitle = today.strftime('%d %b %Y')

    if 'application/json' in request.META.get('HTTP_ACCEPT'):
        stories_dict = map(lambda story: story.to_dict(), stories)
        dump = json.dumps({
            'stories': stories_dict,
            'subtitle': subtitle
        })
        return HttpResponse(dump, content_type='application/json')
    else:
        return render(request, 'services/front_page.html', {'stories': stories, 'subtitle': subtitle})


@cache_page(60)
def index(request, slug):
    today = timezone.now()
    print('oijoi')
    return day(request, slug, today.year, today.month, today.day)


@cache_page(5 * 60)
def year(request, slug, year):
    service = get_object_or_404(Service, slug=slug)
    queryset = service.stories \
        .filter(status=Story.OK, date__year=year) \
        .values('url', 'title') \
        .annotate(score=Sum('score'), date=Min('date')) \
        .order_by('-score')
    return stories(request, service, queryset, year)


@cache_page(5 * 60)
def month(request, slug, year, month):
    service = get_object_or_404(Service, slug=slug)
    queryset = service.stories \
        .filter(status=Story.OK, date__year=year, date__month=month) \
        .values('url', 'title') \
        .annotate(score=Sum('score'), date=Min('date')) \
        .order_by('-score')
    subtitle = timezone.datetime(int(year), int(month), 1).strftime('%b %Y')
    return stories(request, service, queryset, subtitle)


@cache_page(5 * 60)
def day(request, slug, year, month, day):
    date = datetime.datetime(int(year), int(month), int(day))
    service = get_object_or_404(Service, slug=slug)
    queryset = service.stories.filter(status=Story.OK, date=date)[:10]
    subtitle = timezone.datetime(int(year), int(month), int(day)).strftime('%d %b %Y')
    return stories(request, service, queryset, subtitle)


@cache_page(60 * 60)
def archive(request, slug):
    service = get_object_or_404(Service, slug=slug)

    dates = service.stories.all().order_by('-date').values_list('date', flat=True)
    str_dates = map(lambda date: date.strftime('%Y-%m-%d'), dates)
    str_dates = remove_duplicates(str_dates)

    archive = OrderedDict()
    for year, months in groupby(str_dates, lambda date: date[:4]):
        archive[year] = OrderedDict()
        for month, days in groupby(months, lambda date: date[5:7]):
            archive[year][month] = list()
            for day in days:
                archive[year][month].append(day[8:10])

    if 'application/json' in request.META.get('HTTP_ACCEPT'):
        dump = json.dumps(archive)
        return HttpResponse(dump, content_type='application/json')
    else:
        return render(request, 'services/archive.html', {
            'service': service,
            'archive': archive
        })
