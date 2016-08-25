from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User
from articles.models import Post, Comment

class HomePageView(TemplateView):
    template_name = "articles/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-view_count')
        return context

class PostView(generic.DetailView):
    template_name = "articles/post.html"
    model = Post
    context_object_name = "post_title"

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context['post'] = self.object
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
        context['comments'] = Comment.objects.filter(user=self.object)
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
    

    

