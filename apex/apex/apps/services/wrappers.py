import logging
import re

from django.conf import settings
from django.utils import timezone

import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

class AbstractBaseClient:
    def __init__(self):
        self.headers = {'user-agent':'apex/1.0'}

class HackerNewsClient(AbstractBaseClient):
    base_url = 'https://hacker-news.firebaseio.com'

    def request(self,endpoint):
        r = requests.get(endpoint,headers=self.headers)
        result = r.json()
        return result

    def get_top_stories(self):
        endpoint = '%s/v0/topstories.json' % self.base_url
        return self.request(endpoint)

    def get_story(self,code):
        endpoint = '%s/v0/item/%s.json' % (self.base_url, code)
        return self.request(endpoint)

    def get_max_item(self):
        endpoint = '%s/v0/maxitem.json' % self.base_url
        return self.request(endpoint)

    
class RedditClient(AbstractBaseClient):

    def get_front_page_stories(self):
        stories = list()


        try:
            r = requests.get('https://www.reddit.com/.json',headers=self.headers)
            result = r.json()
            stories = result['data']['children']
        except ValueError:
            logger.exception('An error ocuured while executing RedditClient.get_front_page_stories')

        return stories

### ADD more APIs 
