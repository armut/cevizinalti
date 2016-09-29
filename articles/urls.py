from django.conf.urls import url

from . import views

app_name = 'articles'
urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^login$', views.loginView, name='login'),
    url(r'^logout$', views.logoutView, name='logout'),

    url(r'^user/(?P<pk>\d+)/$', views.UserView.as_view(), name='user'),
    url(r'^category/(?P<slug>[-\w]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', views.PostView.as_view(), name='post'),

    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/fav/$', views.fav, name='fav'),
]
