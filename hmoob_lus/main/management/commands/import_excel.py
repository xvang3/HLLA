import pandas as pd
from django.core.management.base import BaseCommand
from main.models import Word
from pathlib import Path

class Command(BaseCommand):
    help = 'Import words from an Excel file'

    def handle(self, *args, **kwargs):
        # Get the path three levels above this file
        base_path = Path(__file__).resolve().parents[3]  # Move up 3 levels
        excel_path = base_path / 'PDF HLLA.xlsx'  # Append the filename to the base path

        # Load the Excel file
        df = pd.read_excel(excel_path)

        # Loop through each row and update or create Word objects
        for index, row in df.iterrows():
            if pd.notna(row['English Word']) and pd.notna(row['Hmong Word']):
                # Update or create the Word object
                word, created = Word.objects.update_or_create(
                    english_word=row['English Word'],
                    hmong_word=row['Hmong Word'],
                    defaults={
                        'category': row['Category'] if pd.notna(row['Category']) else None,
                        'male_audio_url': row['Male Audio'] if pd.notna(row['Male Audio']) else None,
                        'female_audio_url': row['Female Audio'] if pd.notna(row['Female Audio']) else None,
                        'pronunciation_video_url': row['Pronunciation Video'] if pd.notna(row['Pronunciation Video']) else None,
                        'real_video_url': row['Real Video'] if pd.notna(row['Real Video']) else None,
                        'animated_video_url': row['Animated Video'] if pd.notna(row['Animated Video']) else None,
                        'image_filename': row['Image Filename'] if pd.notna(row['Image Filename']) else None,
                    }
                )
                print(f"{'Created' if created else 'Updated'} word: {word.english_word}")
