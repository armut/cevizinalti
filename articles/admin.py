from django.contrib import admin
from .models import Post, Comment, Genre, Whoami, Fav

class FilterUsers(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(FilterUsers, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(author=request.user)
        else:
            return qs

    def has_change_permission(self, request, obj=None):
        if not obj or request.user.is_superuser:
            return True
        return obj.author == request.user

class PostAdmin(FilterUsers):
    prepopulated_fields = { 'slug': ('title',) }

class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('name',)  }

class WhoamiAdmin(FilterUsers):
    pass

class FavAdmin(FilterUsers):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Whoami, WhoamiAdmin)
admin.site.register(Fav, FavAdmin)

