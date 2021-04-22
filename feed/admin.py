from django.contrib import admin

from .models import Comment, Post


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


# noinspection PyMethodMayBeStatic
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'date_created', 'is_edited', 'date_edited', 'post_privacy', 'author', 'comment_count', 'reaction_count')
    ordering = ('id', 'post', 'date_created', 'is_edited', 'date_edited', 'post_privacy', 'author')
    search_fields = ('post', 'author__username')
    list_filter = ('is_edited', 'date_created', 'post_privacy')
    list_display_links = ('id', 'post')
    inlines = [CommentInline, ]

    def comment_count(self, obj):
        return obj.comments.all().count()

    def reaction_count(self, obj):
        return obj.likes.all().count()


# noinspection PyMethodMayBeStatic
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment', 'post', 'date_created', 'is_edited', 'date_edited', 'author', 'reaction_count')
    ordering = ('id', 'comment', 'post', 'date_created', 'is_edited', 'date_edited', 'author')
    search_fields = ('comment', 'author__username')
    list_filter = ('is_edited', 'date_created')
    list_display_links = ('id', 'comment', 'post')

    def reaction_count(self, obj):
        return obj.likes.all().count()
