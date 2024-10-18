from django.db import models

# Create your models here.

from django.db import models

class Word(models.Model):
    # Fields for English and Hmong words
    english_word = models.CharField(max_length=255)
    hmong_word = models.CharField(max_length=255)

    # Optional fields for uploading audio and video files
    male_audio_file = models.FileField(upload_to='audio/', blank=True, null=True)  # Optional
    female_audio_file = models.FileField(upload_to='audio/', blank=True, null=True)  # Optional
    pronunciation_video_file = models.FileField(upload_to='videos/', blank=True, null=True)  # Optional
    real_video_file = models.FileField(upload_to='videos/', blank=True, null=True)  # Optional
    animated_video_file = models.FileField(upload_to='videos/', blank=True, null=True)  # Optional

    def __str__(self):
        return f"{self.english_word}"

class Alphabet(models.Model):
    # Field for the letter
    letter = models.CharField(max_length=255)

    # Optional fields for uploading audio and video files
    male_audio_file = models.FileField(upload_to='audio/', blank=True, null=True)  # Optional
    female_audio_file = models.FileField(upload_to='audio/', blank=True, null=True)  # Optional
    pronunciation_video_file = models.FileField(upload_to='videos/', blank=True, null=True)  # Optional

    def __str__(self):
        return f"{self.letter}"
