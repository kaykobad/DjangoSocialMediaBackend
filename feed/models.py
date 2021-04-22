from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

USER = get_user_model()


class Post(models.Model):
    post = models.TextField()
    date_created = models.DateTimeField(editable=False)
    is_edited = models.BooleanField(default=False)
    date_edited = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(USER, on_delete=models.CASCADE, related_name='posts')
    attachment = models.FileField(upload_to='post_attachments/', null=True, blank=True)
    post_privacy = models.CharField(max_length=20, default='friends')
    likes = models.ManyToManyField(USER, blank=True, related_name='likes')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.id:
            self.date_created = timezone.now()
        else:
            self.is_edited = True
            self.date_edited = timezone.now()
        return super(Post, self).save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.post


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    date_created = models.DateTimeField(editable=False)
    is_edited = models.BooleanField(default=False)
    date_edited = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(USER, on_delete=models.CASCADE, related_name='my_comments')
    attachment = models.FileField(upload_to='comment_attachments/', null=True, blank=True)
    likes = models.ManyToManyField(USER, blank=True, related_name='comment_likes')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.id:
            self.date_created = timezone.now()
        else:
            self.is_edited = True
            self.date_edited = timezone.now()
        return super(Comment, self).save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.comment

