import os
import string

import dj_database_url
from decouple import Csv, config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# ==============================================================================
# CORE SETTINGS
# ==============================================================================

SECRET_KEY = 'r#*x&hnz3qu9t*5k^5d8^i_uav6_%9!9toy$f@2q+egz6nd%9&'


#SECRET_KEY = config('SECRET_KEY', default=string.ascii_letters)

DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1,localhost', cast=Csv())

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    'apex.apps.accounts',
    'apex.apps.core',
    'apex.apps.externalfeed',
    'apex.apps.services',
    'widget_tweaks',

]

ROOT_URLCONF = 'apex.urls'

WSGI_APPLICATION = 'apex.wsgi.application'

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL', default='sqlite:///%s' % os.path.join(BASE_DIR, 'db.sqlite3'))
    )
}

INTERNAL_IPS = [
    '127.0.0.1',
]


# ==============================================================================
# MIDDLEWARE SETTINGS
# ==============================================================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ==============================================================================
# TEMPLATES SETTINGS
# ==============================================================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'apex/templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apex.apps.services.context_processors.services',
            ],
        },
    },
]

# ==============================================================================
# INTERNATIONALIZATION AND LOCALIZATION SETTINGS
# ==============================================================================

LANGUAGE_CODE = config('LANGUAGE_CODE', default='en-us')

TIME_ZONE = config('TIME_ZONE', default='UTC')

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('en-us', 'English'),
    ('pt-br', 'Portuguese'),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'apex/locale'),
)


# ==============================================================================
# STATIC FILES SETTINGS
# ==============================================================================

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'apex/static'),
]


# ==============================================================================
# MEDIA FILES SETTINGS
# ==============================================================================

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')


# ==============================================================================
# AUTHENTICATION AND AUTHORIZATION SETTINGS
# ==============================================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LOGIN_URL = 'login'

LOGOUT_URL = 'logout'

LOGIN_REDIRECT_URL = 'front_page'


# ==============================================================================
# CACHE SETTINGS
# ==============================================================================

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}


# ==============================================================================
# THIRD-PARTY APPS SETTINGS
# ==============================================================================

NYTIMES_API_KEY = config('NYTIMES_API_KEY', default='7txQr6vATslGYYoGh7pZ7ZD424T77cQD')

GOOGLE_NEWS_KEY=config('GOOGLE_NEWS_KEY',default='ffb8a867858a410cb805e3cd7e6134fd')

BBC_SPORT_KEY=config('BBC_SPORT_KEY',default='ffb8a867858a410cb805e3cd7e6134fd')

ENTERTAINMENT_KEY=config('ENTERTAINMENT_KEY',default='ffb8a867858a410cb805e3cd7e6134fd')

BUSINESS_KEY=config('BUSINESS_KEY',default='ffb8a867858a410cb805e3cd7e6134fd')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

FEED_SOURCES = (
    # (key, source, prefix to strip from the url)
    # ('bbchealth',
    #  'http://feeds.bbci.co.uk/news/health/rss.xml',
    #  'http://www.bbc.co.uk/news'),
    # (
    # 'bbcscience',
    #  'http://feeds.bbci.co.uk/news/science_and_environment/rss.xml',
    #  'http://www.bbc.co.uk/news'),
    (
    'sciencedaily',
     'https://www.sciencedaily.com/rss/top/health.xml',
     'http://www.bbc.co.uk/news'),
)

# EMAIL_HOST = 'smtp.sendgrid.net'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'testsite_app'
# EMAIL_HOST_PASSWORD = 'mys3cr3tp4ssw0rd'
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = 'TestSite Team <noreply@example.com>'