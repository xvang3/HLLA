from django.shortcuts import render
from .models import Word
import random

def home(request):
    return render(request, 'home.html')
    
def play_audio_test(request):
    words = Word.objects.all()  # Retrieve all Word objects from the database
    return render(request, 'play_audio_test.html', {'words': words})

def about(request):
    return render(request, 'about.html')

def courses(request):
    return render(request, 'courses.html')

def practice(request):
    return render(request, 'practice.html')

def resources(request):
    return render(request, 'resources.html')

def memory_game(request):
    # Get a sample of words for the game
    words = list(Word.objects.all())
    random.shuffle(words)
    
    # Duplicate each word pair and shuffle again
    game_words = words[:6]  # Adjust the number based on desired difficulty
    card_pairs = [(word.hmong_word, word.english_word) for word in game_words]
    cards = [item for pair in card_pairs for item in pair]  # Flatten the list
    random.shuffle(cards)

    return render(request, 'memory_game.html', {'cards': cards})
