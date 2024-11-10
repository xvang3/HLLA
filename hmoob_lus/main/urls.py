from django.urls import path
from . import views

urlpatterns = [
    path('audio-test/', views.play_audio_test, name='audio_test'),  # Ensure this exists
    path('', views.home, name='home'),  # Home page view
    path('about/', views.about, name='about'),  # About page
    path('courses/', views.courses, name='courses'),  # Course page
    path('practice/', views.practice, name='practice'),  # Practice page
    path('resources/', views.resources, name='resources'),  # Resources page
    
    path('units/tones/', views.vowels_consonants, name='u1_tones'), # Course Units
    path('units/vowels_and_consonants/', views.vowels_consonants, name='vowels_consonants'),
    path('units/vowels/', views.vowels_consonants, name='u2_vowels'),
    path('units/consonants/', views.vowels_consonants, name='u3_consonants'),
    path('units/phrases/', views.phrases, name='u4_phrases'),
    path('units/numbers/', views.numbers, name='u5_numbers'),
    path('units/family/', views.family, name='u6_family'),
    path('units/animals/', views.animals, name='u7_animals'),

    path('practice/tones/', views.tones, name='p1_tones'), # Practice Units
    path('practice/vowels/', views.vowels, name='p2_vowels'),
    path('practice/consonants/', views.consonants, name='p3_consonants'),
    path('practice/phrases/', views.phrases, name='p4_phrases'),
    path('practice/numbers/', views.numbers, name='p5_numbers'),
    path('practice/family/', views.family, name='p6_family'),
    path('practice/animals/', views.animals, name='p7_animals'),
    # Add other URLs as needed
]