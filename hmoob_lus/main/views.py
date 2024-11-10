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
    words = Word.objects.filter(category="Tones")
    return render(request, 'practice/p1_tones.html', {'words': words})

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

def p4_numbers(request):
    words = Word.objects.filter(category="Numbers")
    return render(request, 'practice/p4_numbers.html', {'words': words})

def p5_family(request):
    words = Word.objects.filter(category="Family")
    return render(request, 'practice/p5_family.html', {'words': words})

def p6_animals(request):
    words = Word.objects.filter(category="Animals")
    return render(request, 'practice/p6_animals.html', {'words': words})