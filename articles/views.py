from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count

from django.contrib.auth.models import User
from articles.models import Image, Fav, Whoami, Genre, Post, Comment

class HomePageView(TemplateView):
    template_name = "articles/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-date')
        context['popular_posts'] = Post.objects.all().order_by('-view_count')[:3]
        context['genres'] = Genre.objects.all().annotate(posts_in_this_genre=Count('post')).order_by('name')
        context['genre_in_question'] = 'home'
        return context


class CategoryView(generic.DetailView):
    template_name = "articles/genre.html"
    model = Genre
    context_object_name = "category";

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['genre_in_question'] = self.object
        context['genres'] = Genre.objects.all().annotate(posts_in_this_genre=Count('post')).order_by('name')
        context['othergenres'] = Genre.objects.all().exclude(name=self.object.name).annotate(posts_in_this_genre=Count('post')).order_by('name')
        context['description'] = self.object.description
        context['posts'] = Post.objects.filter(genre=self.object).order_by('-view_count')
        context['comments'] = Comment.objects.filter(post__genre=self.object)[:3]
        return context


class PostView(generic.DetailView):
    template_name = "articles/post.html"
    model = Post
    context_object_name = "post_title"

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context['post'] = self.object
        context['images'] = Image.objects.filter(post=self.object)
        context['genre_in_question'] = self.object.genre
        context['genres'] = Genre.objects.all().annotate(posts_in_this_genre=Count('post')).order_by('name')
        context['comments'] = Comment.objects.filter(post=self.object)

        self.object.view_count += 1
        self.object.save()

        most_popular = Post.objects.filter().order_by('-view_count')[0]
        context['most_popular_post'] = most_popular
        return context

class UserView(generic.DetailView):
    template_name = "articles/user.html"
    model = User
    context_object_name = "user"

    def get_context_data(self, **kwargs):
        context = super(UserView, self).get_context_data(**kwargs)
        context['user'] = self.object
        context['posts'] = Post.objects.filter(author=self.object).order_by("-view_count")
        context['genres'] = Genre.objects.all().annotate(posts_in_this_genre=Count('post')).order_by('name')
        context['comments'] = Comment.objects.filter(user=self.object)

        try:
            context['whoami'] = Whoami.objects.filter(author=self.object)[0]
        except IndexError:
            context['whoami'] = None

        return context


@require_http_methods(['POST'])
def loginView(request):
    uid = request.POST.get('uid')
    passwd = request.POST.get('pass')

    user = authenticate(username=uid, password=passwd)
    if user is not None:
        if user.is_active:
            login(request, user)
            msg = "成功！"
        else:
            msg = "doğru şifre yanlış şey"
    else:
        # needs something like login error page.
        msg = "ne kullanıcı adı ne de şifre doğru"

    return JsonResponse({"msg": msg})

@csrf_exempt
@require_http_methods(['POST'])
def logoutView(request):
    logout(request)
    msg = "成功！"
    return JsonResponse({"msg": msg})
    

@csrf_exempt
@require_http_methods(['POST'])
def fav(request, **kwargs):
    msg = ""
    try:
        Fav.objects.get(author=request.user, post__slug=kwargs["slug"]).delete()
        msg = "Successfully unfav'd"
    except:
        Fav(author=request.user, post=Post.objects.get(slug=kwargs["slug"])).save()
        msg = "Successfully fav'd"
    return JsonResponse({"msg": msg})
