from django.db import models

from core.models import AuditModel, User


class VisibilityOptions(models.TextChoices):
    PUBLIC = 'public'
    INVITE_ONLY = 'invite_only'
    FRIENDS = 'friends'
    FAMILY = 'family'


class Address(models.Model):
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    country = models.CharField(max_length=255)


class Event(AuditModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    visibility = models.CharField(max_length=255, choices=VisibilityOptions.choices)
    visibility_group = models.ManyToManyField(User, related_name='visibility_group', blank=True)

    def save(self, *args, **kwargs):
        match self.visibility:
            case Visibility.PUBLIC:
                # Intent: Public event visible to all users, no filter if enum is used in downstream queries.
                self.visibility_group.clear()
            case Visibility.INVITE_ONLY:
                # Intent: Restricted event, begins only with the creator and will be appended later as invites are sent.
                self.visibility_group.set([self.created_by])
            case Visibility.FRIENDS:
                self.visibility_group.set([self.created_by] + list(self.created_by.friends.all()))
            case Visibility.FAMILY:
                self.visibility_group.set([self.created_by] + list(self.created_by.family.all()))
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-start_date_time']
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
