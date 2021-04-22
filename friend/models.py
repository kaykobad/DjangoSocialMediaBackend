from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

USER = get_user_model()


class FriendRequest(models.Model):
    sender = models.ForeignKey(USER, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(USER, on_delete=models.CASCADE, related_name='receiver')
    request_send_date = models.DateTimeField()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.request_send_date = timezone.now()
        super(FriendRequest, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

    class Meta:
        verbose_name = "Friend Request"
        verbose_name_plural = "Friend Requests"


class FriendshipMapper(models.Model):
    user_1 = models.ForeignKey(USER, on_delete=models.CASCADE, related_name='user1')
    user_2 = models.ForeignKey(USER, on_delete=models.CASCADE, related_name='user2')
    request_accept_date = models.DateTimeField()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.request_accept_date = timezone.now()
        super(FriendshipMapper, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

    class Meta:
        verbose_name = "Friendship"
        verbose_name_plural = "Friendship Manager"


class BlockedUser(models.Model):
    blocker = models.ForeignKey(USER, on_delete=models.CASCADE, related_name='blocker')
    blocked = models.ForeignKey(USER, on_delete=models.CASCADE, related_name='blocked')
    block_date = models.DateTimeField()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.block_date = timezone.now()
        super(BlockedUser, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

    class Meta:
        verbose_name = "Blocked User"
        verbose_name_plural = "Blocked Users"
