from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Booking
from .forms import BookingForm

from django.shortcuts import render

def landing_page(request):
    return render(request, 'ersteapp/landing_page.html')

def calendar_view(request):
    bookings = Booking.objects.filter(approved=True)
    return render(request, 'ersteapp/calendar.html', {'bookings': bookings})

@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('calendar')
    else:
        form = BookingForm()
    return render(request, 'ersteapp/create_booking.html', {'form': form})