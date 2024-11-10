from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('audio-test/', views.play_audio_test, name='audio_test'),  # Ensure this exists
    path('', views.home, name='home'),  # Home page view
    path('about/', views.about, name='about'),  # About page
    path('courses/', views.courses, name='courses'),  # Course page
    path('practice/', views.practice, name='practice'),  # Practice page
    path('resources/', views.resources, name='resources'),  # Resources page
    path('units/vowels_and_consonants/', views.vowels_consonants, name='vowels_consonants'),
    path('practice/tones/', views.tones, name='tones'),
    path('practice/vowels/', views.vowels, name='vowels'),
    path('practice/consonants/', views.consonants, name='consonants'),
    path('practice/animals/', views.animals, name='animals'),
    path('practice/numbers/', views.numbers, name='numbers'),
    path('practice/phrases/', views.phrases, name='phrases'),
    path('practice/family/', views.family, name='family'),
    path('memory-game/', views.memory_game, name='memory_game'),  # Add this line

    # Add other URLs as needed
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
