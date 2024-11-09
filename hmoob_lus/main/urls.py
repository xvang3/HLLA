from django.urls import path
from . import views

urlpatterns = [
    path('audio-test/', views.play_audio_test, name='audio_test'),  # Ensure this exists
    path('', views.home, name='home'),  # Home page view
    path('about/', views.about, name='about'),  # About page
    path('courses/', views.courses, name='courses'),  # Course page
    path('practice/', views.practice, name='practice'),  # Practice page
    path('resources/', views.resources, name='resources'),  # Resources page
    path('practice/animals/', views.animals, name='animals'),
    path('practice/numbers/', views.numbers, name='numbers'),
    path('practice/phrases/', views.phrases, name='phrases'),
    path('practice/family/', views.family, name='family'),
    # Add other URLs as needed
]