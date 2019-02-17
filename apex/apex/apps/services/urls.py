from django.urls import path


from apex.apps.services import views
from django.conf.urls import include, url

app_name = 'services'


urlpatterns = [
    url(r'^$', views.index, name='index'),
    #path(' ', views.index,name='index'),
    path('archive/', views.archive, name='archive'),
    path('<int:year>/',views.year, name='year'),
    path('<int:year>/<int:month>',views.month, name='month'),
    path('<int:year>/<int:month>/<int:day>/',views.day,name='day'),
]