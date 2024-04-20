from django.urls import path
from .views import login_view, logout_view, registration_view


urlpatterns = [
    path('login/', login_view, name='login-p'),
    path('logout/', logout_view, name='logout-p'),
    path('registration/', registration_view, name='register-p'),
]