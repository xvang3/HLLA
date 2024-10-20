from django.urls import path
from . import views

urlpatterns = [
    path('audio-test/', views.play_audio_test, name='audio_test'),  # Ensure this exists
    path('', views.home, name='home'),  # Home page view
    # Add other URLs as needed
]