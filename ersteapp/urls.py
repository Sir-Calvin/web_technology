from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('create-booking/', views.create_booking, name='create_booking'),
    path('', views.landing_page, name='landing_page'),
    path('calendar/', views.calendar_view, name='calendar'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]