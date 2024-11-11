from django.db import models

class Word(models.Model):
    english_word = models.CharField(max_length=255)
    hmong_word = models.CharField(max_length=255)
    category = models.CharField(max_length=255, blank=True, null=True)

    # Update fields to match the Excel data structure
    male_audio_url = models.TextField(blank=True, null=True)
    female_audio_url = models.TextField(blank=True, null=True)
    pronunciation_video_url = models.TextField(blank=True, null=True)
    real_video_url = models.TextField(blank=True, null=True)
    animated_video_url = models.TextField(blank=True, null=True)

    image_filename = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.english_word}"



class Alphabet(models.Model):
    letter = models.CharField(max_length=255)

    # Fields for storing audio and video URLs
    male_audio_url = models.TextField(blank=True, null=True)
    female_audio_url = models.TextField(blank=True, null=True)
    pronunciation_video_url = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.letter}"

