from django.conf.urls import url

from . import views

app_name = 'articles'
urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^login$', views.loginView, name ='login'),
    url(r'^logout$', views.logoutView, name ='logout'),
    url(r'^(?P<slug>[-\w]+)', views.PostView.as_view(), name='post')
]
