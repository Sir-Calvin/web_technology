from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('register/', views.register, name='register'),
    path('calendar/', views.calendar_view, name='calendar'),
    path('create_booking/', views.create_booking, name='create_booking'),
]