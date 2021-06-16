"""Model core."""
# Django
import uuid

from django.db import models


class TimesModelMixin(models.Model):
    """Core base model.
    CoreModel acts as an abstract base class from which every
    other model in the project will inherit. This class provides
    every table with the following attributes:
        + created (DateTime): Store the datetime the object was created.
        + modified (DateTime): Store the last datetime the object was modified.
    """

    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created.'
    )
    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on which the object was last modified.'
    )

    class Meta:
        """Meta option."""
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']


class UUIDModelMixin(models.Model):
    """Provides uuid field."""
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:  # noqa
        abstract = True
