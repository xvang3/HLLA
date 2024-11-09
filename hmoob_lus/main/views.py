from django.shortcuts import render
from .models import Word

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
    words = Word.objects.all()  
    return render(request, 'practice.html', {'words': words})

def resources(request):
    return render(request, 'resources.html')

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