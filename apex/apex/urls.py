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
from django.urls import include, path
from apex.apps.core import views as core_views
from apex.apps.services import views as services_views
from apex.templates.services.includes import views as B_view

from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apex.apps.services.models import BookmarkArticle
from apex.apps.services.views  import successView, feedbackView, aboutView, searchView, searchResultView

urlpatterns = [
    path('', services_views.front_page, name='front_page'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('signup/', services_views.register_user, name='signup'),
    path('feedback/', services_views.feedbackView, name='feedback'),
    path('success/', successView, name='success'),
    path('about/', aboutView, name='about'),
    path('search/',searchView,name='search'),
    path('about/', TemplateView.as_view(template_name='core/about.html'), name='about'),
    path('status/', core_views.status, name='status'),
    path('cookies/', TemplateView.as_view(template_name='core/cookies.html'), name='cookies'),
    path('privacy/', TemplateView.as_view(template_name='core/privacy.html'), name='privacy'),
    path('FAQ/', TemplateView.as_view(template_name='core/FAQ.html'), name='FAQ'),
    path('terms/', TemplateView.as_view(template_name='core/terms.html'), name='terms'),
    path('bookmarks/',B_view.BookmarksView.as_view(),name='bookmarks'),
    path('<slug:slug>/', include('apex.apps.services.urls', namespace='services')),
    path('<pk>/bookmark/',services_views.BookmarkView.as_view(model=BookmarkArticle),
        name='article_bookmark'),
    # url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    # url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     auth_views.password_reset_confirm, name='password_reset_confirm'),
    # url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),

    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    #path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
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
