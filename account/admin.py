from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import TokenProxy

from .forms import UserCreationForm, UserChangeForm
from .models import User, TokenManager

# Unregister unnecessary models
admin.site.unregister(Group)
admin.site.unregister(TokenProxy)


@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # Admin Display
    list_display = ('id', 'first_name', 'last_name', 'email', 'date_joined', 'country', 'religion', 'language')
    list_filter = ('is_active', 'is_staff', 'date_joined', 'last_login', 'religion', 'language')
    search_fields = ('first_name', 'last_name', 'email', 'country', 'religion', 'language')
    ordering = ('id', 'first_name', 'last_name', 'email', 'date_joined', 'country', 'religion', 'language')
    list_display_links = ('id', 'first_name', 'last_name')

    # Field Sets
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'country', 'language', 'religion', 'avatar')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {
            'fields': ('last_login', )
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'country', 'religion', 'language'),
        }),
    )


# @admin.register(TokenManager)
# class TokenManagerAdmin(admin.ModelAdmin):
#     # Admin Display
#     list_display = ('key', 'email', 'date_created')
#     list_filter = ('date_created', )
#     search_fields = ('key', 'email')
#     ordering = ('key', 'email', 'date_created')
#     list_display_links = ('key', 'email')
