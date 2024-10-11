from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Booking
from datetime import date, time

class BookingModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.booking = Booking.objects.create(
            user=self.user,
            date=date.today(),
            time=time(14, 0),
            details='Test booking',
            approved=False
        )

    def test_booking_creation(self):
        self.assertEqual(self.booking.user.username, 'testuser')
        self.assertEqual(self.booking.details, 'Test booking')
        self.assertFalse(self.booking.approved)

    def test_booking_str(self):
        self.assertEqual(str(self.booking), f"{self.booking.date} {self.booking.time} - {self.booking.user.username}")

class BookingViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.booking = Booking.objects.create(
            user=self.user,
            date=date.today(),
            time=time(14, 0),
            details='Test booking',
            approved=True
        )

    def test_calendar_view(self):
        response = self.client.get(reverse('calendar'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test booking')

    def test_create_booking_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('create_booking'), {
            'date': date.today(),
            'time': time(15, 0),
            'details': 'Another test booking'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful booking creation
        self.assertTrue(Booking.objects.filter(details='Another test booking').exists())