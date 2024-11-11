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
    # Get parameters from the request
    new_game = request.GET.get('newGame', 'false').lower() == 'true'
    shuffle = request.GET.get('shuffle', 'false').lower() == 'true'

    # Initialize cards list
    cards = []

    if new_game:
        # Fetch a completely new set of 8 unique words and store it in the session
        words = list(Word.objects.all())
        game_cards = random.sample(words, 8)
        request.session['game_cards'] = [game_card.id for game_card in game_cards]
    else:
        # Retrieve the same set from session for shuffle or first-time loading
        word_ids = request.session.get('game_cards')
        if word_ids:
            game_cards = Word.objects.filter(id__in=word_ids)
        else:
            # Fallback in case there's no game set in the session
            words = list(Word.objects.all())
            game_cards = random.sample(words, 8)
            request.session['game_cards'] = [game_card.id for game_card in game_cards]

    # Build the cards, with each word added as Hmong-English pairs
    for game_card in game_cards:

        # Randomly choose between male and female audio if both are available
        audio_url = None
        if game_card.male_audio_url and game_card.female_audio_url:
            chosen_audio = random.choice(['male', 'female'])
            if chosen_audio == 'male' and game_card.male_audio_url:
                audio_url = settings.MEDIA_URL + game_card.male_audio_url
            elif chosen_audio == 'female' and game_card.female_audio_url:
                audio_url = settings.MEDIA_URL + game_card.female_audio_url
        elif game_card.male_audio_url:
            audio_url = settings.MEDIA_URL + game_card.male_audio_url
        elif game_card.female_audio_url:
            audio_url = settings.MEDIA_URL + game_card.female_audio_url

        cards.append({
            'id': f"{game_card.id}-hmong", 
            'word': game_card.hmong_word,
            'audio_url': audio_url,})
        cards.append({
            'id': f"{game_card.id}-english", 
            'word': game_card.english_word,
            'audio_url': None})

    # Shuffle only if shuffle parameter is true or if it's the first time loading
    if shuffle or new_game:
        random.shuffle(cards)

    # Pass the cards and total pairs to the template
    return render(request, 'memory_game.html', {'cards': cards, 'total_pairs': len(game_cards)})

