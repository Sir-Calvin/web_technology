from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),  # Landingpage-URL hinzufügen
    path('calendar/', views.calendar_view, name='calendar'),
    path('create_booking/', views.create_booking, name='create_booking'),
]