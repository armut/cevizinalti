from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    content = models.TextField()
    date = models.DateTimeField()
    genre = models.CharField(max_length=30)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200)

    def get_absolute_url(self):
        return reverse('articles:post', args=[self.slug])

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.TextField()

    def __str__(self):
        return self.post.title + " ~ "  + self.comment_text[:20] + "..." 

