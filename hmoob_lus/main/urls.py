from django.urls import path
from . import views

urlpatterns = [
    path('audio-test/', views.play_audio_test, name='audio_test'),  # Ensure this exists
    path('', views.home, name='home'),  # Home page view
    path('about/', views.about, name='about'),  # About page
    path('courses/', views.courses, name='courses'),  # Course page
    path('practice/', views.practice, name='practice'),  # Practice page
    path('resources/', views.resources, name='resources'),  # Resources page

    # Add other URLs as needed
]