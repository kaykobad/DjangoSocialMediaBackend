"""DjangoSocialMediaBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from configuration.views import ConfigurationViewSet
from feedback.views import FeedBackViewSet
from account.views import AuthViewSet, ProfileViewSet
from friend.views import FriendViewSet
from feed.views import FeedViewSet

# Configure Site Titles
admin.site.site_header = "Django Social Media"
admin.site.site_title = "Django Social Media"
admin.site.index_title = "Welcome to Admin Portal"

# API Routes
router = routers.DefaultRouter()
router.register('api/account/auth', AuthViewSet, basename='authentication')
router.register('api/account/profile', ProfileViewSet, basename='user_profile')
router.register('api/configuration', ConfigurationViewSet, basename='configurations')
router.register('api/feedback', FeedBackViewSet, basename='all_feedback')
router.register('api/friends', FriendViewSet, basename='friend')
router.register('api/feed', FeedViewSet, basename='feeds')

urlpatterns = [
    path('', admin.site.urls),
] + router.urls

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
