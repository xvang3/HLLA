from django.shortcuts import render
from .models import Word
import random

def home(request):
    return render(request, 'home.html')
    
def play_audio_test(request):
    words = Word.objects.all()
    return render(request, 'play_audio_test.html', {
        'words': words,
        'MEDIA_URL': settings.MEDIA_URL
    })

def about(request):
    return render(request, 'about.html')

def courses(request):
    return render(request, 'courses.html')

def practice(request):
    words = Word.objects.all()  
    return render(request, 'practice.html', {'words': words})

def resources(request):
    return render(request, 'resources.html')

def memory_game(request):
    # Get a random sample of words from the Word model
    words = list(Word.objects.all())
    random.shuffle(words)
    
    # Take the first 6 words (3 pairs)
    game_cards = words[:6]
    cards = []
    
    for game_card in game_cards:
        # Each word is added twice with unique IDs for matching purposes
        cards.append({'id': f"{game_card.id}-hmong", 'word': game_card.hmong_word})
        cards.append({'id': f"{game_card.id}-english", 'word': game_card.english_word})
    
    # Shuffle the cards again for the game layout
    random.shuffle(cards)

    # Pass the shuffled cards to the template
    return render(request, 'memory_game.html', {'cards': cards, 'total_pairs': len(game_cards)})

def tones(request):
    words = Word.objects.filter(category="Tones")
    return render(request, 'tones.html', {'words': words})

def vowels_consonants(request):
    return render(request, 'vowels_consonants.html')

def vowels(request):
    words = Word.objects.filter(category="Vowels")
    return render(request, 'vowels.html', {'words': words})

def consonants(request):
    words = Word.objects.filter(category="Consonants")
    return render(request, 'consonants.html', {'words': words})

def animals(request):
    words = Word.objects.filter(category="Animals")
    return render(request, 'animals.html', {'words': words})

def numbers(request):
    words = Word.objects.filter(category="Numbers")
    return render(request, 'numbers.html', {'words': words})

def phrases(request):
    words = Word.objects.filter(category="Common Phrases")
    return render(request, 'phrases.html', {'words': words})

def family(request):
    words = Word.objects.filter(category="Family")
    return render(request, 'family.html', {'words': words})