from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField()
    slug = models.SlugField(max_length=100, db_index=True)

    def get_absolute_url(self):
        return reverse('articles:category', args=[self.slug])

    def __str__(self):
        return self.name

class Post(models.Model):
    content = models.TextField()
    date = models.DateTimeField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    view_count = models.PositiveIntegerField()
    slug = models.SlugField(max_length=200)

    def get_absolute_url(self):
        return reverse('articles:post', kwargs={'year': self.date.year, 'month': self.date.strftime('%m'), 'day': self.date.strftime('%d'), 'slug': self.slug})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    comment_text = models.TextField()

    def __str__(self):
        return self.post.title + " ~ "  + self.comment_text[:20] + "..." 


class Whoami(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    short_bio = models.TextField()

    def __str__(self):
        return (self.short_bio[:10] + "...")

