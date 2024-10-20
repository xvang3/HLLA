from django.core.management.base import BaseCommand
from main.models import Word

class Command(BaseCommand):
    help = 'Clear the Word table'

    def handle(self, *args, **kwargs):
        Word.objects.all().delete()
        self.stdout.write('All words deleted successfully.')
