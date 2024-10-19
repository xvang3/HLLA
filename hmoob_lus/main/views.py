from django.shortcuts import render
from .models import Word

def play_audio_test(request):
    # Retrieve all Word objects with audio files (for testing purposes)
    words_with_audio = Word.objects.exclude(male_audio_file__isnull=True).exclude(male_audio_file='')

    return render(request, 'play_audio_test.html', {'words': words_with_audio})
