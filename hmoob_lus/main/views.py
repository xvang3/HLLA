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

def phrases(request):
    words = Word.objects.filter(category="Common Phrases")
    return render(request, 'units/u4_phrases.html', {'words': words})

def numbers(request):
    words = Word.objects.filter(category="Numbers")
    return render(request, 'units/u5_numbers.html', {'words': words})

def family(request):
    words = Word.objects.filter(category="Family")
    return render(request, 'units/u6_family.html', {'words': words})

def animals(request):
    words = Word.objects.filter(category="Animals")
    return render(request, 'units/u7_animals.html', {'words': words})

def phrases(request):
    words = Word.objects.filter(category="Common Phrases")
    return render(request, 'practice/p4_phrases.html', {'words': words})

def numbers(request):
    words = Word.objects.filter(category="Numbers")
    return render(request, 'practice/p5_numbers.html', {'words': words})

def family(request):
    words = Word.objects.filter(category="Family")
    return render(request, 'practice/p6_family.html', {'words': words})

def animals(request):
    words = Word.objects.filter(category="Animals")
    return render(request, 'practice/p7_animals.html', {'words': words})