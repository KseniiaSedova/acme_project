from django.contrib.auth import views
from django.urls import path

from .views import UserRegistration


urlpatterns = [
    path('auth/registration/', UserRegistration.as_view(),
         name='registration'),
]
