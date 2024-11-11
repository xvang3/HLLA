from django.shortcuts import render
from .models import Word
import random
from django.conf import settings

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
    #Get a random sample of words from the Word model
    words = list(Word.objects.all())
    random.shuffle(words)
    
    
    #Take the first 6 words (3 pairs)
    game_cards = words[:6]
    cards = []

    for game_card in game_cards:
        cards.append({
            'id': f"{game_card.id}-hmong",
            'word': game_card.hmong_word,
            'type': 'hmong',
            'audio_url': f"{settings.MEDIA_URL}{game_card.male_audio_url}"
        })
        
        # Each word is added twice with unique IDs for matching purposes
        cards.append({
            'id': f"{game_card.id}-english",
            'word': game_card.english_word,
            'type': 'english'
        })

    #Shuffle the cards again for the game layout
    random.shuffle(cards)

    # Pass the shuffled cards to the template
    return render(request, 'memory_game.html', {
        'cards': cards,
        'total_pairs': len(game_cards)
    })

