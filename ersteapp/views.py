from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegisterForm, BookingForm
from .models import Booking
from django.contrib.auth.decorators import login_required

def landing_page(request):
    return render(request, 'ersteapp/landing_page.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Account created for {user.username}!')
            return redirect('calendar')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

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