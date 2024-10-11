from django.contrib import admin
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'time', 'approved')
    list_filter = ('approved', 'date')
    search_fields = ('user__username', 'details')

admin.site.register(Booking, BookingAdmin)