"""apex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.views.generic import TemplateView
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.urls import include, path
from django.views.generic.edit import CreateView
from apex.apps.core import views as core_views
from apex.apps.services import views as services_views
from apex.apps.services.models import BookmarkArticle
from apex.apps.services.views  import successView, feedbackView, aboutView

urlpatterns = [
    path('', services_views.front_page, name='front_page'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('signup/', CreateView.as_view(template_name='registration/signup.html',form_class=UserCreationForm,success_url='/'), name='signup'),
    path('feedback/', services_views.feedbackView,name='feedback'),
    path('success/', successView, name='success'),
    path('about/',aboutView,name='about'),
    path('about/', TemplateView.as_view(template_name='core/about.html'), name='about'),
    path('status/', core_views.status, name='status'),
    path('cookies/', TemplateView.as_view(template_name='core/cookies.html'), name='cookies'),
    path('privacy/', TemplateView.as_view(template_name='core/privacy.html'), name='privacy'),
    path('terms/', TemplateView.as_view(template_name='core/terms.html'), name='terms'),
    path('bookmarks/',TemplateView.as_view(template_name='bookmarks.html'),name='bookmarks'),
    path('<slug:slug>/', include('apex.apps.services.urls', namespace='services')),
    path('<pk>/bookmark/',services_views.BookmarkView.as_view(model=BookmarkArticle),
        name='article_bookmark'),
    # url('bbc-sport/article/(?P<pk>\d+)/bookmark/',services_views.BookmarkView.as_view(model=BookmarkArticle),
    #     name='article_bookmark'),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    try:
        import debug_toolbar
        urlpatterns = [
            path('__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
    except ImportError:
        print()
        pass
