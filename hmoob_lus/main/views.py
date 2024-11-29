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

def about(request): #take out if not added later
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
        audio_url = f"{settings.MEDIA_URL}{random.choice([game_card.male_audio_url, game_card.female_audio_url])}"

        cards.append({
            'id': f"{game_card.id}-hmong",
            'word': game_card.hmong_word,
            'type': 'hmong',
            'audio_url': audio_url
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


def u1_tones(request):
    words = Word.objects.filter(category="Tones")
    return render(request, 'units/u1_tones.html', {'words': words})

def u2_vowels_consonants(request):
    return render(request, 'units/u2_vowels_consonants.html')

def u2_vowels(request):
    words = Word.objects.filter(category="Vowels")
    return render(request, 'units/u2_vowels.html', {'words': words})

def u2_consonants(request):
    words = Word.objects.filter(category="Consonants")
    return render(request, 'units/u2_consonants.html', {'words': words})

def u3_phrases(request):
    words = Word.objects.filter(category="Common Phrases")
    return render(request, 'units/u3_phrases.html', {'words': words})

def u4_numbers(request):
    words = Word.objects.filter(category="Numbers")
    return render(request, 'units/u4_numbers.html', {'words': words})

def u5_family(request):
    words = Word.objects.filter(category="Family")
    return render(request, 'units/u5_family.html', {'words': words})

def u6_animals(request):
    words = Word.objects.filter(category="Animals")
    return render(request, 'units/u6_animals.html', {'words': words})

def p1_tones(request):
    words = Word.objects.filter(category="Tone Markers")
    return render(request, 'practice/p1_tones.html', {'words': words})

def p1_tones_cards(request):
    words = Word.objects.filter(category="Tone Markers")
    return render(request, 'practice/p1_tones_cards.html', {'words': words})

def p1_tones_audio(request):
    words = Word.objects.filter(category="Tone Markers")
    return render(request, 'practice/p1_tones_audio.html', {
        'words': words,
        'MEDIA_URL': settings.MEDIA_URL 
    })

def p2_vowels_consonants(request):
    return render(request, 'practice/p2_vowels_consonants.html')

def p2_vowels(request):
    words = Word.objects.filter(category="Vowels")
    return render(request, 'practice/p2_vowels.html', {'words': words})

def p2_consonants(request):
    words = Word.objects.filter(category="Consonants")
    return render(request, 'practice/p2_consonants.html', {'words': words})

def p3_phrases(request):
    words = Word.objects.filter(category="Common Phrases")
    return render(request, 'practice/p3_phrases.html', {'words': words})

def p3_phrases_cards(request):
    words = Word.objects.filter(category="Common Phrases")
    return render(request, 'practice/p3_phrases_cards.html', {'words': words})

def p3_phrases_audio(request):
    words = Word.objects.filter(category="Common Phrases")
    return render(request, 'practice/p3_phrases_audio.html', {
        'words': words,
        'MEDIA_URL': settings.MEDIA_URL 
    })

def p4_numbers(request):
    words = Word.objects.filter(category="Numbers")
    return render(request, 'practice/p4_numbers.html', {'words': words})

def p4_numbers_cards(request):
    words = Word.objects.filter(category="Numbers")
    return render(request, 'practice/p4_numbers_cards.html', {'words': words})

def p4_numbers_audio(request):
    words = Word.objects.filter(category="Numbers")
    return render(request, 'practice/p4_numbers_audio.html', {
        'words': words,
        'MEDIA_URL': settings.MEDIA_URL 
    })

def p5_family(request):
    words = Word.objects.filter(category="Family")
    return render(request, 'practice/p5_family.html', {'words': words})

def p5_family_cards(request):
    words = Word.objects.filter(category="Family")
    return render(request, 'practice/p5_family_cards.html', {'words': words})

def p5_family_audio(request):
    words = Word.objects.filter(category="Family")
    return render(request, 'practice/p5_family_audio.html', {
        'words': words,
        'MEDIA_URL': settings.MEDIA_URL 
    })

def p6_animals(request):
    words = Word.objects.filter(category="Animals")
    return render(request, 'practice/p6_animals.html', {'words': words})

def p6_animals_cards(request):
    words = Word.objects.filter(category="Animals")
    return render(request, 'practice/p6_animals_cards.html', {'words': words})

def p6_animals_audio(request):
    words = Word.objects.filter(category="Animals")
    return render(request, 'practice/p6_animals_audio.html', {
        'words': words,
        'MEDIA_URL': settings.MEDIA_URL 
    })