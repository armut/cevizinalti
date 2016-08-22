from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import generic

from articles.models import Post, Comment

class HomePageView(TemplateView):
    template_name = "articles/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context

class PostView(generic.DetailView):
    template_name = "articles/post.html"
    model = Post
    context_object_name = "post_title"

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context['post'] = self.object
        return context
