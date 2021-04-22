from django.contrib import admin
from .models import FriendRequest, FriendshipMapper, BlockedUser


@admin.register(FriendRequest)
class FriendRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'request_send_date')
    list_filter = ('request_send_date',)
    search_fields = ('sender__email', 'sender__first_name', 'receiver__email', 'receiver__first_name')
    ordering = ('id', 'sender', 'receiver', 'request_send_date')
    list_display_links = ('id', 'sender')


@admin.register(FriendshipMapper)
class FriendshipMapperAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_1', 'user_2', 'request_accept_date')
    list_filter = ('request_accept_date',)
    search_fields = ('user_1__email', 'user_1__first_name', 'user_2__email', 'user_2__first_name')
    ordering = ('id', 'user_1', 'user_2', 'request_accept_date')
    list_display_links = ('id', 'user_1')


@admin.register(BlockedUser)
class BlockedUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'blocker', 'blocked', 'block_date')
    list_filter = ('block_date',)
    search_fields = ('blocker__email', 'blocker__first_name', 'blocked__email', 'blocked__first_name')
    ordering = ('id', 'blocker', 'blocked', 'block_date')
    list_display_links = ('id', 'blocker')
