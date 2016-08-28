from django.conf.urls import url

from . import views

app_name = 'articles'
urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^login$', views.loginView, name ='login'),
    url(r'^logout$', views.logoutView, name ='logout'),

    url(r'^category/(?P<slug>[-\w]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^category/(?P<genre>[-\w]+)/(?P<slug>[-\w]+)/$', views.PostView.as_view(), name='post'),
    url(r'^user/(?P<pk>)/$', views.UserView.as_view(), name='user')
]
