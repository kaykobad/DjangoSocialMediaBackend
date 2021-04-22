from django.contrib.auth import get_user_model
from rest_framework import serializers

from account.serializers import UserSerializer
from .models import FriendRequest, FriendshipMapper, BlockedUser

USER = get_user_model()


class AllFriendsSerializer(serializers.Serializer):
    friend = UserSerializer()
    friend_since = serializers.DateTimeField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class AllSentRequestSerializer(serializers.ModelSerializer):
    receiver = UserSerializer()

    class Meta:
        model = FriendRequest
        fields = ('id', 'receiver', 'request_send_date')


class AllReceivedRequestSerializer(serializers.ModelSerializer):
    sender = UserSerializer()

    class Meta:
        model = FriendRequest
        fields = ('id', 'sender', 'request_send_date')


class SearchUserSerializer(serializers.Serializer):
    search_keyword = serializers.CharField(max_length=240, write_only=True)
    user = UserSerializer(read_only=True)
    is_friend = serializers.BooleanField(read_only=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
