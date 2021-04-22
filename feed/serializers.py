from rest_framework import serializers

from account.serializers import UserSerializer
from .models import Post, Comment


# noinspection PyMethodMayBeStatic
class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False, read_only=True)
    total_likes = serializers.SerializerMethodField()
    total_comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'post', 'date_created', 'is_edited', 'date_edited', 'author', 'total_likes', 'total_comments', 'attachment', 'post_privacy')
        read_only_fields = ('id', 'date_created', 'is_edited', 'date_edited', 'author', 'total_likes', 'total_comments')

    def get_total_comments(self, obj):
        return obj.comments.count()

    def get_total_likes(self, obj):
        return obj.likes.count()

    def validate_post_privacy(self, value):
        privacy_options = ('public', 'friends')
        if value is None or value == '':
            return privacy_options[1]
        if value not in privacy_options:
            raise serializers.ValidationError(f'Privacy option must be one of these: {privacy_options}')
        return value


# noinspection PyMethodMayBeStatic
class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False, read_only=True)
    post_id = serializers.IntegerField(source='post.id', required=False)
    post_text = serializers.CharField(source='post.post', read_only=True)
    total_likes = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'comment', 'author', 'post_id', 'post_text', 'date_created', 'is_edited', 'date_edited', 'attachment', 'total_likes')
        read_only_fields = ('id', 'author', 'post_text', 'date_created', 'is_edited', 'date_edited')

    def get_total_likes(self, obj):
        return obj.likes.count()
