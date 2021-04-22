from random import shuffle

from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from account.serializers import UserSerializer
from .models import FriendRequest, FriendshipMapper, BlockedUser
from .serializers import (
    AllFriendsSerializer,
    AllSentRequestSerializer,
    AllReceivedRequestSerializer,
    SearchUserSerializer
)

USER = get_user_model()


class FriendViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated, ]

    @action(methods=['POST', ], detail=False, url_path='send-friend-request/(?P<user_id>[^/.]+)', permission_classes=[IsAuthenticated, ])
    def send_friend_request(self, request, user_id):
        try:
            sender = request.user
            receiver = USER.objects.get(id=user_id)
            text = 'Success! Friend request sent.'
            if sender.id == receiver.id:
                text = 'Error! You can not send friend request to yourself.'
            elif FriendRequest.objects.filter(sender=sender, receiver=receiver).count() > 0:
                text = 'You have already sent a friend request to this person.'
            elif FriendRequest.objects.filter(receiver=sender, sender=receiver).count() > 0:
                text = 'You have already received a friend request from this person.'
            elif FriendshipMapper.objects.filter(Q(user_1=sender, user_2=receiver) | Q(user_1=receiver, user_2=sender)).count() > 0:
                text = 'You are already friend with this person.'
            else:
                FriendRequest.objects.create(sender=sender, receiver=receiver)
        except ObjectDoesNotExist:
            text = 'Error! Receiver does not exists.'
        return Response(data={'detail': text}, status=status.HTTP_200_OK)

    @action(methods=['GET', ], detail=False, url_path='get-all-friends', permission_classes=[IsAuthenticated, ])
    def get_all_friends(self, request):
        friends = FriendshipMapper.objects.filter(Q(user_1=request.user) | Q(user_2=request.user))
        serialized_data = []

        for f in friends:
            if f.user_1 == request.user:
                data = {'friend': f.user_2, 'friend_since': f.request_accept_date}
            else:
                data = {'friend': f.user_1, 'friend_since': f.request_accept_date}
            serialized_data.append(AllFriendsSerializer(data).data)
        return Response(data={'all_friends': serialized_data}, status=status.HTTP_200_OK)

    @action(methods=['GET', ], detail=False, url_path='get-all-sent-request', permission_classes=[IsAuthenticated, ])
    def get_all_sent_request(self, request):
        sent_requests = FriendRequest.objects.filter(sender=request.user)
        data = {'all_sent_requests': AllSentRequestSerializer(sent_requests, many=True).data}
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['GET', ], detail=False, url_path='get-all-received-request', permission_classes=[IsAuthenticated, ])
    def get_all_received_request(self, request):
        sent_requests = FriendRequest.objects.filter(receiver=request.user)
        data = {'all_received_requests': AllReceivedRequestSerializer(sent_requests, many=True).data}
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['POST', ], detail=False, url_path='un-friend/(?P<user_id>[^/.]+)', permission_classes=[IsAuthenticated, ])
    def un_friend(self, request, user_id):
        try:
            friend = FriendshipMapper.objects.get(Q(user_1=request.user, user_2__id=user_id) | Q(user_1__id=user_id, user_2=request.user))
            friend.delete()
            data = {'detail': 'Success! You have been un-friend.'}
        except ObjectDoesNotExist:
            data = {'detail': 'Error! you are not friend with this person.'}
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['POST', ], detail=False, url_path='accept-friend-request/(?P<friend_request_id>[^/.]+)', permission_classes=[IsAuthenticated, ])
    def accept_friend_request(self, request, friend_request_id):
        try:
            friend_request = FriendRequest.objects.get(id=friend_request_id, receiver=request.user)
            FriendshipMapper.objects.create(user_1=request.user, user_2=friend_request.sender)
            friend_request.delete()
            data = {"detail": "Success! Friend request accepted."}
            return Response(data=data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            data = {"detail": "Error! Friend request does not exist."}
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['POST', ], detail=False, url_path='reject-friend-request/(?P<friend_request_id>[^/.]+)', permission_classes=[IsAuthenticated, ])
    def reject_friend_request(self, request, friend_request_id):
        try:
            friend_request = FriendRequest.objects.get(id=friend_request_id, receiver=request.user)
            friend_request.delete()
            data = {"detail": "Success! Friend request rejected."}
            return Response(data=data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            data = {"detail": "Error! Friend request does not exist."}
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['POST', ], detail=False, url_path='cancel-friend-request/(?P<friend_request_id>[^/.]+)', permission_classes=[IsAuthenticated, ])
    def cancel_friend_request(self, request, friend_request_id):
        try:
            friend_request = FriendRequest.objects.get(id=friend_request_id, sender=request.user)
            friend_request.delete()
            data = {"detail": "Success! Friend request cancelled."}
            return Response(data=data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            data = {"detail": "Error! Friend request does not exist."}
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['GET', ], detail=False, url_path='friend-suggestions', permission_classes=[IsAuthenticated, ])
    def friend_suggestions(self, request):
        try:
            friends = FriendshipMapper.objects.filter(Q(user_1=request.user) | Q(user_2=request.user))
            blocked = BlockedUser.objects.filter(Q(blocker=request.user) | Q(blocked=request.user))
            excluded = [request.user.id]
            for f in friends:
                excluded.append(f.user_2.id if f.user_1 == request.user else f.user_1.id)
            for b in blocked:
                excluded.append(b.blocked.id if b.blocker == request.user else b.blocker.id)
            user_list = list(USER.objects.all().exclude(id__in=excluded))
            shuffle(user_list)
            if len(user_list) > 20:
                user_list = user_list[:20]
            data = {"suggestions": UserSerializer(user_list, many=True).data}
            return Response(data=data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            data = {"detail": "Error! Something went wrong. Please try again."}
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['POST', ], detail=False, url_path='search-people', permission_classes=[IsAuthenticated, ])
    def search_people(self, request):
        serializer = SearchUserSerializer(data=request.data)
        if serializer.is_valid():
            keyword = serializer.validated_data['search_keyword']
            all_profiles = USER.objects.filter(
                Q(first_name__icontains=keyword) |
                Q(email__icontains=keyword)
            ).exclude(id=request.user.id)

            friends = FriendshipMapper.objects.filter(Q(user_1=request.user) | Q(user_2=request.user))
            blocked = BlockedUser.objects.filter(Q(blocker=request.user) | Q(blocked=request.user))

            current_friends = []
            blocked_users = []
            serialized_data = []
            for f in friends:
                current_friends.append(f.user_2 if f.user_1 == request.user else f.user_1)
            for b in blocked:
                blocked_users.append(b.blocked if b.blocker == request.user else b.blocker)
            for u in all_profiles:
                if u in blocked_users:
                    continue
                data = {'user': u, 'is_friend': True if u in current_friends else False}
                serialized_data.append(SearchUserSerializer(data).data)
            return Response(data={'search_result': serialized_data}, status=status.HTTP_200_OK)
        else:
            return Response(data={'detail': 'Error! Something went wrong. Please try again later.'}, status=status.HTTP_200_OK)

    @action(methods=['POST', ], detail=False, url_path='block/(?P<user_id>[^/.]+)', permission_classes=[IsAuthenticated, ])
    def block_user(self, request, user_id):
        try:
            user = USER.objects.get(id=user_id)
            if user == request.user:
                text = 'Error! You can not block yourself.'
            elif BlockedUser.objects.filter(Q(blocked=user, blocker=request.user) | Q(blocker=user, blocked=request.user)).count() > 0:
                text = 'Error! User is already blocked or user doesn\'t exist.'
            else:
                if FriendshipMapper.objects.filter(user_1=request.user, user_2=user).count() > 0:
                    FriendshipMapper.objects.get(user_1=request.user, user_2=user).delete()
                elif FriendshipMapper.objects.filter(user_2=request.user, user_1=user).count() > 0:
                    FriendshipMapper.objects.get(user_2=request.user, user_1=user).delete()
                elif FriendRequest.objects.filter(sender=request.user, receiver=user).count() > 0:
                    FriendRequest.objects.get(sender=request.user, receiver=user).delete()
                elif FriendRequest.objects.filter(receiver=request.user, sender=user).count() > 0:
                    FriendRequest.objects.get(receiver=request.user, sender=user).delete()
                BlockedUser.objects.create(blocker=request.user, blocked=user)
                text = 'Success! User is blocked.'
        except ObjectDoesNotExist:
            text = 'Error! User does not exist.'
        return Response(data={'detail': text}, status=status.HTTP_200_OK)

    @action(methods=['POST', ], detail=False, url_path='unblock/(?P<user_id>[^/.]+)', permission_classes=[IsAuthenticated, ])
    def un_block(self, request, user_id):
        try:
            blocked = BlockedUser.objects.get(blocker=request.user, blocked__id=user_id)
            blocked.delete()
            text = 'Success! User is unblocked.'
        except ObjectDoesNotExist:
            text = 'Error! Blocked user does not exist.'
        return Response(data={'detail': text}, status=status.HTTP_200_OK)

    @action(methods=['GET', ], detail=False, url_path='get-blocked-users', permission_classes=[IsAuthenticated, ])
    def get_blocked_users(self, request):
        blocked = BlockedUser.objects.filter(blocker=request.user)
        serialized_data = []
        for u in blocked:
            serialized_data.append(UserSerializer(u.blocked).data)
        return Response(data={'blocked_users': serialized_data}, status=status.HTTP_200_OK)
