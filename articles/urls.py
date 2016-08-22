from django.conf.urls import url

from . import views

app_name = 'articles'
urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^(?P<slug>[-\w]+)', views.PostView.as_view(), name='post')
]
