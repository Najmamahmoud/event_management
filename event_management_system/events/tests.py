from django.test import TestCase
from django.urls import reverse
from .models import Event
from .forms import EventForm

class EventModelTests(TestCase):
    def setUp(self):
        self.event = Event.objects.create(name="Test Event", date="2024-12-31")

    def test_event_creation(self):
        """Test that the event is created correctly."""
        event = Event.objects.get(name="Test Event")
        self.assertEqual(event.name, "Test Event")
        self.assertEqual(event.date, "2024-12-31")

class EventViewsTests(TestCase):
    def setUp(self):
        self.event = Event.objects.create(name="Test Event", date="2024-12-31")

    def test_event_detail_view(self):
        """Test that the event detail view returns a 200 response and contains the event name."""
        url = reverse('event_detail', args=[self.event.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.event.name)

    def test_event_list_view(self):
        """Test that the event list view returns a 200 response and contains the event name."""
        url = reverse('list_events')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.event.name)

class EventFormTests(TestCase):
    def test_valid_form(self):
        form_data = {'name': 'Test Event', 'date': '2024-12-31'}
        form = EventForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {'name': '', 'date': '2024-12-31'}
        form = EventForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
