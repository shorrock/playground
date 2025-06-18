from typing import Any, Optional

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.query import QuerySet


class User(AbstractUser):
    pass
    friends = models.ManyToManyField("core.User", related_name='friend_to', blank=True)
    family = models.ManyToManyField("core.User", related_name='family_to', blank=True)


class AuditModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def delete(self) -> None:
        self.is_deleted = True
        self.save()

    class Meta:
        abstract = True
