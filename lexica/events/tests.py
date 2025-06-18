from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from core.models import User
from events.models import Event, VisibilityOptions

class EventTestCase(TestCase):
    def setUp(self):
        self.ian_user = User.objects.create(first_name="Ian", last_name="Shorrock", email="ian@test.com")
        self.john_user = User.objects.create(first_name="John", last_name="Does", email="john@test.com")
        ian_user.friends.add(self.john_user)
        '''
        class Address(models.Model):
            address_line_1 = models.CharField(max_length=255)
            address_line_2 = models.CharField(max_length=255, null=True, blank=True)
            city = models.CharField(max_length=255)
            state = models.CharField(max_length=255)
            zip_code = models.CharField(max_length=255)
            country = models.CharField(max_length=255)
        '''
        ians_address = Address.objects.create(
            address_line_1="123 Peach Way",
            city="Cityville",
            state="Colorado",
            zip_code="12345",
            country="United States"
        )
        '''
        class Event(AuditModel):
            name = models.CharField(max_length=255)
            description = models.TextField()
            created_by = models.ForeignKey(User, on_delete=models.CASCADE)
            start_date_time = models.DateTimeField()
            end_date_time = models.DateTimeField()
            location = models.CharField(max_length=255)
            address = models.ForeignKey(Address, on_delete=models.CASCADE)
            visibility = models.CharField(max_length=255, choices=Visibility.choices)
            visibility_group = models.ManyToManyField(User, related_name='visibility_group', blank=True)
        '''
        start_time = timezone.now()
        end_time = start_time + timedelta(hours=6)
        self.test_event = Event.objects.create(
            name="Game Night!",
            description="Let's play games",
            created_by=ian_user,
            start_date_time=start_time,
            end_date_time=end_time,
            location="Ian's house",
            address=ians_address,
            visibility=VisibilityOptions.FRIENDS,
        )
    
    def test_event_visibility(self):
        assert self.test_event.visibility == VisibilityOptions.FRIENDS
        assert self.test_event.visibility_group == self.ian_user.friends
