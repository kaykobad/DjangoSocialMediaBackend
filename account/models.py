from __future__ import unicode_literals

import string
import random

from django.conf import settings
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=120, blank=True)
    last_name = models.CharField(_('last name'), max_length=120, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    country = models.CharField(max_length=255, blank=True)
    language = models.CharField(max_length=255, blank=True)
    religion = models.CharField(max_length=255, blank=True)
    is_blocked = models.BooleanField(default=False, blank=True)
    avatar = models.ImageField(upload_to='profile_pictures/', blank=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff status'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=settings.DEFAULT_FROM_EMAIL, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


class TokenManager(models.Model):
    key = models.CharField(max_length=8, primary_key=True)
    email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        TokenManager.objects.filter(email=self.email).delete()
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    @classmethod
    def generate_key(cls):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    def __str__(self):
        return self.key + ' - ' + self.email

    def validate_token(self):
        seconds_diff = (timezone.now() - self.date_created).total_seconds()
        if seconds_diff < settings.TOKEN_TIMEOUT:
            self.delete()
            return True
        else:
            return False

    def send_email(self, subject, message, from_email=settings.DEFAULT_FROM_EMAIL, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def send_sms(self, sms_text):
        # TODO: Add sms sending text here
        pass

    class Meta:
        verbose_name = 'Token Manager'
        verbose_name_plural = 'Tokens Manager'

