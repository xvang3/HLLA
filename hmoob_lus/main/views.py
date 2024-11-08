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
