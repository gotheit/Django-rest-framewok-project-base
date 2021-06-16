"""User model."""
# Django
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils import timezone

# Utilities
from apps.core.models import TimesModelMixin, UUIDModelMixin


class CustomUserManager(BaseUserManager):
    """Django user creation modification, allows creating user without the need for username."""

    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """Creates and saves a User with the given email and password."""
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a User with the given email and password."""
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Creates and saves a Super User with the given email and password."""
        return self._create_user(email, password, True, True,
                                 **extra_fields)


class User(TimesModelMixin, UUIDModelMixin, AbstractUser):
    """User model.
    Extend from Django's Abstract User, change  email and add some extra fields.
    """
    username = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )

    is_active = models.BooleanField(default=True)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    ordering = ('email',)
    REQUIRED_FIELDS = ['first_name', 'last_name']

    is_client = models.BooleanField(
        'client',
        default=True,
        help_text=(
            'Help easily distinguish users and perform queries. '
            'Clients are the main type of user.'
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default=True,
        help_text='Set to true when the user have verified its email address.'
    )

    def __str__(self):
        """Return username."""
        return self.email
