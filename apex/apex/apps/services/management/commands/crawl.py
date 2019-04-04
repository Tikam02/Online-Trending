import time

from django.conf import settings
from django.core.management.base import BaseCommand

from apex.apps.services import crawlers


class Command(BaseCommand):
    help = 'Crawl external services to update top stories'

    def get_crawler_class(self, slug):
        crawlers_classes = {
            'reddit': crawlers.RedditCrawler,
            'hn': crawlers.HackerNewsCrawler,
            'nytimes': crawlers.NYTimesCrawler,
            'google-news': crawlers.GoogleNewsCrawler,
            'bbc-sport': crawlers.BBCSportCrawler,
            'entertainment-weekly': crawlers.EntertainmentCrawler,
           # 'Business-Insider': crawlers.BusinessCrawler,
        }
        return crawlers_classes.get(slug)

    def add_arguments(self, parser):
        parser.add_argument('service_slug', nargs='+', type=str, help='Service Slug')

    def handle(self, *args, **kwargs):
        service_slugs = kwargs['service_slug']
        for slug in service_slugs:
            if slug == 'nytimes' and not settings.NYTIMES_API_KEY:
                self.stdout.write(self.style.ERROR(
                    'The nytimes crawler is missing API Key. '
                    'Read more: https://github.com/vitorfs/woid#the-new-york-times'
                ))
                continue

            if slug == 'google-news' and not settings.GOOGLE_NEWS_KEY:
                self.stdout.write(self.style.ERROR(
                    'The GoogleNews crawler is missing API Key. '
                ))
                continue

            if slug == 'bbc-sport' and not settings.BBC_SPORT_KEY:
                self.stdout.write(self.style.ERROR(
                    'The BBCSport crawler is missing API Key. '
                ))
                continue

            if slug == 'entertainment-weekly' and not settings.ENTERTAINMENT_KEY:
                self.stdout.write(self.style.ERROR(
                    'The Entertainment Crawler is missing API Key. '
                ))
                continue

            """if slug == 'Business-Insider' and not settings.BUSINESS_KEY:
                self.stdout.write(self.style.ERROR(
                    'The Business Crawler is missing API Key. '
                ))
                continue"""

            crawler_class = self.get_crawler_class(slug)

            if crawler_class is not None:
                crawler = crawler_class()
                start_time = time.time()
                crawler.run()
                elapsed_seconds = round(time.time() - start_time, 2)
                self.stdout.write(self.style.SUCCESS('%s crawler executed in %s seconds') % (slug, elapsed_seconds))
            else:
                self.stdout.write(self.style.WARNING('Crawler with slug "%s" not found.') % slug)
