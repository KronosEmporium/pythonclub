from django.test import TestCase
from clubapp.models import Meeting, MeetingMinutes, Resource, Event
from clubapp.views import index, getmeetings, getminutes, getresources, getevents, meetingdetails
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.
class MeetingTest(TestCase):
    def test_string(self):
        meet = Meeting(meetingtitle = "Book Club")
        self.assertEqual(str(meet), meet.meetingtitle)
        
    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), "meeting")

class MeetingMinutesTest(TestCase):
    def setup(self):
        meet = Meeting(meetingtitle = "Knitting Club")
        minutes = MeetingMinutes(meeting = meet, minutes = "We had a bunch of fun knitting.")
        return minutes

    def test_meeting(self):
        minute = self.setup()
        self.assertEqual(str(minute.meeting), "Knitting Club")

    def test_table(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), "minutes")

class ResourceTest(TestCase):
    def test_string(self):
        res = Resource(resourcename = "Administration")
        self.assertEqual(str(res), res.resourcename)

    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), "resource")

class EventTest(TestCase):
    def test_string(self):
        eve = Event(eventtitle = "Hackathon 2019")
        self.assertEqual(str(eve), eve.eventtitle)

    def test_table(self):
        self.assertEqual(str(Event._meta.db_table), "event")

class IndexTest(TestCase):
    def test_view_url_accessible(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

class GetMeetingsTest(TestCase):
    def test_view_url_accessible(self):
        response = self.client.get(reverse("meetings"))
        self.assertEqual(response.status_code, 200)

    def setup(self):
        u = User.objects.create(username = 'myuser')
        meet = Meeting.objects.create(meetingtitle = "Book Club", meetingdate = "2019-04-03", meetingtime = "12:00", location = "here", agenda = "an agenda")
        return meet
    
    def test_meeting_detail_success(self):
        deets = self.setup()
        response = self.client.get(reverse("meetingdetails", args = (deets.id,)))
        self.assertEqual(response.status_code, 200)

class GetMinutesTest(TestCase):
    def test_view_url_accessible(self):
        response = self.client.get(reverse("minutes"))
        self.assertEqual(response.status_code, 200)

class GetResourcesTest(TestCase):
    def test_view_url_accessible(self):
        response = self.client.get(reverse("resources"))
        self.assertEqual(response.status_code, 200)

class GetEventsTest(TestCase):
    def test_view_url_accessible(self):
        response = self.client.get(reverse("events"))
        self.assertEqual(response.status_code, 200)

class New_Meeting_authentication_test(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username = 'testuser1', password = 'P@ssw0rd1')
        self.type = Meeting.objects.create(meetingtitle = "Fun Meeting", meetingdate = "2019-04-03", meetingtime = "11:00", location = "USA", agenda = "Stuff.")

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('newmeeting'))
        self.assertRedirects(response, '/accounts/login/?next=/clubapp/newMeeting/')

    def test_Logged_in_uses_correct_template(self):
        login = self.client.login(username = 'testuser1', password = 'P@ssw0rd1')
        response = self.client.get(reverse('newmeeting'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'clubapp/newmeeting.html')