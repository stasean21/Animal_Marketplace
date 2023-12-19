# animals/management/commands/import_animals.py
from django.core.management.base import BaseCommand
from animals.models import Animal
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Import animals into the database'

    def handle(self, *args, **kwargs):
        # Ваши данные о животных
        animals_data = [
            {'name': 'Кролик3', 'species': 'Кролик', 'description': 'Забавный кролик', 'is_available': True,
             'price': 40.0, 'image': '/Users/admin/Desktop/animal_marketplace/animal_images/кролик 1.jpeg', 'city': 'Ваш город',
             'created_at': datetime.now() - timedelta(days=19)},
        ]

        # Массово создаем животных
        Animal.objects.bulk_create([Animal(**animal_data) for animal_data in animals_data])

        self.stdout.write(self.style.SUCCESS('Successfully imported animals'))
