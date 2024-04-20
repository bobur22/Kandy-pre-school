from django.urls import path
from .views import home_view, about_view, team_view, program_view, enroll_view, career_view, contact_view

urlpatterns = [
    path('', home_view, name='home-p'),
    path('about/', about_view, name='about-p'),
    path('team/', team_view, name='team-p'),
    path('programs/', program_view, name='programs-p'),
    path('enrollment/', enroll_view, name='enrollment-p'),
    path('career/', career_view, name='career-p'),
    path('contact/', contact_view, name='contact-p'),
]