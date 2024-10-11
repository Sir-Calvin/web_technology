from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'time', 'approved')
    list_filter = ('approved', 'date')
    search_fields = ('user__username', 'details')

admin.site.register(Booking, BookingAdmin)

# Admin-Seite anpassen
admin.site.site_header = "Band Buchungsverwaltung"
admin.site.site_title = "Band Buchungsverwaltung Admin"
admin.site.index_title = "Willkommen im Admin-Bereich der Band Buchungsverwaltung"