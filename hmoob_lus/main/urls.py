from django.urls import path
from . import views

urlpatterns = [
    path('audio-test/', views.play_audio_test, name='audio_test'),  # Ensure this exists
    path('', views.home, name='home'),  # Home page view
    path('about/', views.about, name='about'),  # About page
    path('courses/', views.courses, name='courses'),  # Course page
    path('practice/', views.practice, name='practice'),  # Practice page
    path('resources/', views.resources, name='resources'),  # Resources page
    
    # path('units/u1_tones/', views.u1_tones, name='u1_tones'), # Course Units
    # path('units/u2_vowels_and_consonants/', views.u2_vowels_consonants, name='u2_vowels_consonants'),
    # path('units/u2_vowels/', views.u2_vowels, name='u2_vowels'),
    # path('units/u2_consonants/', views.u2_consonants, name='u2_consonants'),
    # path('units/u3_phrases/', views.u3_phrases, name='u3_phrases'),
    # path('units/u4_numbers/', views.u4_numbers, name='u4_numbers'),
    # path('units/u5_family/', views.u5_family, name='u5_family'),
    # path('units/u6_animals/', views.u6_animals, name='u6_animals'),

    path('units/u1_tones/', views.u1_tones, name='u1_tones'), # Course Units
    path('units/u2_vowels_and_consonants/', views.u2_vowels_consonants, name='u2_vowels_consonants'),
    path('units/u2_vowels/', views.u2_vowels, name='u2_vowels'),
    path('units/u2_consonants/', views.u2_consonants, name='u2_consonants'),
    path('units/u3_phrases/', views.u3_phrases, name='u3_phrases'),
    path('units/u4_numbers/', views.u4_numbers, name='u4_numbers'),
    path('units/u5_family/', views.u5_family, name='u5_family'),
    path('units/u6_animals/', views.u6_animals, name='u6_animals'),    

    path('practice/p1_tones/', views.p1_tones, name='p1_tones'), # Practice Units
    path('practice/p2_vowels_and_consonants/', views.p2_vowels_consonants, name='p2_vowels_consonants'),
    path('practice/p2_vowels/', views.p2_vowels, name='p2_vowels'),
    path('practice/p2_consonants/', views.p2_consonants, name='p2_consonants'),
    path('practice/p3_phrases/', views.p3_phrases, name='p3_phrases'),
    path('practice/p3_phrases/flashcards/', views.p3_phrases_cards, name='p3_phrases_cards'),
    path('practice/p3_phrases/pronunciations/', views.p3_phrases_audio, name='p3_phrases_audio'),
    path('practice/p4_numbers/', views.p4_numbers, name='p4_numbers'),
    path('practice/p4_numbers/flashcards/', views.p4_numbers_cards, name='p4_numbers_cards'),
    path('practice/p4_numbers/pronunciations/', views.p4_numbers_audio, name='p4_numbers_audio'),
    path('practice/p5_family/', views.p5_family, name='p5_family'),
    path('practice/p5_family/flashcards/', views.p5_family_cards, name='p5_family_cards'),
    path('practice/p5_family/pronunciations', views.p5_family_audio, name='p5_family_audio'),
    path('practice/p6_animals/', views.p6_animals, name='p6_animals'),
    path('practice/p6_animals/flashcards/', views.p6_animals_cards, name='p6_animals_cards'),
    path('practice/p6_animals/pronunciations/', views.p6_animals_audio, name='p6_animals_audio'),
    # Add other URLs as needed
]