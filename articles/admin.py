from django.contrib import admin
from .models import Post, Comment, Genre, Whoami

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('title',) }

class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('name',)  }

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Whoami)

