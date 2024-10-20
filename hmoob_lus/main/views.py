from django.shortcuts import render
from .models import Word

def home(request):
    return render(request, 'home.html')
    
def play_audio_test(request):
    words = Word.objects.all()  # Retrieve all Word objects from the database
    return render(request, 'play_audio_test.html', {'words': words})
