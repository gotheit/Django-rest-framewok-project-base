# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from apps.users.models import User


class CustomUserAdmin(UserAdmin):
    """User model admin."""

    list_display = ('email', 'first_name', 'last_name', 'is_client', 'is_verified')
    ordering = ('email',)
    readonly_fields = ('email',)


admin.site.register(User, CustomUserAdmin)
