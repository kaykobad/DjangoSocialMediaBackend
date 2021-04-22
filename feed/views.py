from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from friend.models import FriendshipMapper
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class FeedViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated, ]

    @action(methods=['POST', ], detail=False, url_path='create-post')
    def create_post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            post = Post(author=request.user)
            for attr, value in serializer.validated_data.items():
                setattr(post, attr, value)
            post.save()
            data = PostSerializer(post).data
            return Response(data=data, status=status.HTTP_200_OK)
        else:
            return Response(data={'detail': 'Error! Something went wrong. Please try again.'}, status=status.HTTP_200_OK)

    @action(methods=['POST', ], detail=False, url_path='update-post/(?P<post_id>[^/.]+)')
    def update_post(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id, author=request.user)
            serializer = PostSerializer(data=request.data)
            if serializer.is_valid():
                for attr, value in serializer.validated_data.items():
                    setattr(post, attr, value)
                post.save()
                likes = post.likes.all().count()
                comments = post.comments.all()
                serialized_comments = CommentSerializer(comments, many=True)
                serialized_post = PostSerializer(post)
                data = serialized_post.data
                data['total_likes'] = likes
                data['total_comments'] = comments.count()
                data['comments'] = serialized_comments.data
                return Response(data=data, status=status.HTTP_200_OK)
            else:
                return Response(data={'detail': 'Error! Something went wrong. Please try again.'}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            data = {'detail': 'Error! No post found. Make sure you are the author of the post and try with a valid post id.'}
            return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['GET', ], detail=False, url_path='my-posts')
    def my_posts(self, request):
        try:
            my_posts = request.user.posts.all()
            return Response(data={'posts': PostSerializer(my_posts, many=True).data}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            data = {'detail': 'Error! Something went wrong. Please try again later.'}
            return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['POST', ], detail=False, url_path='delete-post/(?P<post_id>[^/.]+)')
    def delete_post(self, request, post_id):
        try:
            post = Post.objects.get(author=request.user, id=post_id)
            post.delete()
            return Response(data={'detail': 'Success! Post deleted from database.'}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            data = {'detail': 'Error! Post does not exist.'}
            return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['GET', ], detail=False, url_path='post-details/(?P<post_id>[^/.]+)')
    def post_details(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
            likes = post.likes.all().count()
            comments = post.comments.all()
            serialized_comments = CommentSerializer(comments, many=True)
            serialized_post = PostSerializer(post)
            data = serialized_post.data
            data['total_likes'] = likes
            data['total_comments'] = comments.count()
            data['comments'] = serialized_comments.data
            return Response(data=data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            data = {'detail': 'Error! Post does not exist.'}
            return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['POST', ], detail=False, url_path='like-post/(?P<post_id>[^/.]+)')
    def like_post(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
            if request.user in post.likes.all():
                post.likes.remove(request.user)
                return Response(data={'detail': 'Success! You unliked the post.'}, status=status.HTTP_200_OK)
            post.likes.add(request.user)
            post.save()
            return Response(data={'detail': 'Success! You liked the post.'}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            data = {'detail': 'Error! Post does not exist.'}
            return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['GET', ], detail=False, url_path='my-feed')
    def my_feed(self, request):
        try:
            friends = FriendshipMapper.objects.filter(Q(user_1=request.user) | Q(user_2=request.user))
            posts = Post.objects.none()
            for f in friends:
                if f.user_1 == request.user:
                    posts |= f.user_2.posts.all()
                else:
                    posts |= f.user_1.posts.all()
            return Response(data={'posts': PostSerializer(posts, many=True).data}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            data = {'detail': 'Error! Something went wrong. Please try again later.'}
            return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['POST', ], detail=False, url_path='add-comment')
    def add_comment(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            try:
                post = Post.objects.get(id=serializer.validated_data.pop('post')['id'])
                comment = Comment(
                    author=request.user,
                    post=post
                )
                for attr, value in serializer.validated_data.items():
                    setattr(comment, attr, value)
                comment.save()
                likes = post.likes.all().count()
                comments = post.comments.all()
                serialized_comments = CommentSerializer(comments, many=True)
                serialized_post = PostSerializer(post)
                data = serialized_post.data
                data['total_likes'] = likes
                data['total_comments'] = comments.count()
                data['comments'] = serialized_comments.data
                return Response(data=data, status=status.HTTP_200_OK)
            except Exception:
                data = {"detail": "Could not comment. Invalid post id or comment format."}
                return Response(data=data, status=status.HTTP_200_OK)
        else:
            return Response(data={"detail": "Could not comment. Invalid post id or comment format."}, status=status.HTTP_200_OK)

    @action(methods=['POST', ], detail=False, url_path='update-comment/(?P<comment_id>[^/.]+)')
    def update_comment(self, request, comment_id):
        try:
            comment = Comment.objects.get(id=comment_id, author=request.user)
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid():
                for attr, value in serializer.validated_data.items():
                    setattr(comment, attr, value)
                comment.save()
                post = comment.post
                likes = post.likes.all().count()
                comments = post.comments.all()
                serialized_comments = CommentSerializer(comments, many=True)
                serialized_post = PostSerializer(post)
                data = serialized_post.data
                data['total_likes'] = likes
                data['total_comments'] = comments.count()
                data['comments'] = serialized_comments.data
                return Response(data=data, status=status.HTTP_200_OK)
            else:
                data = {"detail": "Could not update comment. Invalid comment id or format."}
                return Response(data=data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            data = {"detail": "No comment found. Make sure you are the author of the comment."}
            return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['POST', ], detail=False, url_path='delete-comment/(?P<comment_id>[^/.]+)')
    def delete_comment(self, request, comment_id):
        try:
            comment = Comment.objects.get(id=comment_id, author=request.user)
            comment.delete()
            post = comment.post
            likes = post.likes.all().count()
            comments = post.comments.all()
            serialized_comments = CommentSerializer(comments, many=True)
            serialized_post = PostSerializer(post)
            data = serialized_post.data
            data['total_likes'] = likes
            data['total_comments'] = comments.count()
            data['comments'] = serialized_comments.data
            return Response(data=data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            data = {"detail": "Error! No comment found. Make sure you are the author of the comment and try with a valid comment id."}
            return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['POST', ], detail=False, url_path='like-comment/(?P<comment_id>[^/.]+)')
    def like_comment(self, request, comment_id):
        try:
            comment = Comment.objects.get(id=comment_id)
            if request.user not in comment.likes.all():
                comment.likes.add(request.user)
                return Response(data={'detail': 'Success! You liked the comment.'}, status=status.HTTP_200_OK)
            comment.likes.remove(request.user)
            return Response(data={'detail': 'Success! You unliked the comment.'}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            data = {"detail": "Error! No comment found. Try with a valid comment id."}
            return Response(data=data, status=status.HTTP_200_OK)
