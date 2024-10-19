import os
import pandas as pd
from django.core.management.base import BaseCommand
from django.conf import settings
from main.models import Word

class Command(BaseCommand):
    help = 'Import words and their audio/video files from Excel into the database'

    def handle(self, *args, **kwargs):
        # Load the Excel file
        excel_path = 'C:\\Users\\ntxhw\\Downloads\\PDF HLLA.xlsx'
        df = pd.read_excel(excel_path)

        # Iterate through the rows of the Excel file and add them to the database
        for _, row in df.iterrows():
            # Create the Word object
            word = Word.objects.create(
                english_word=row['English Word'],
                hmong_word=row['Hmong Word'],
                category=row['Category'],
                male_audio_file=self.get_file_path(row['Male Audio']),
                female_audio_file=self.get_file_path(row['Female Audio']),
                pronunciation_video_file=self.get_file_path(row['Pronunciation Video']),
                real_video_file=self.get_file_path(row['Real Video']),
                animated_video_file=self.get_file_path(row['Animated Video'])
            )

            self.stdout.write(self.style.SUCCESS(f"Added word: {word.english_word}"))

    def get_file_path(self, file_path):
        """ Helper function to check if file path exists, otherwise return None """
        if pd.isna(file_path):  # If the field is NaN (empty), return None
            return None
        return file_path
