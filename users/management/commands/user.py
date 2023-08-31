from django.core.management.base import BaseCommand
from .users import menu,controllers

class Command(BaseCommand):
    help = 'Menu user'

    
    def handle(self, *args, **options):
        choise = menu()
        controllers(choise)
        self.stdout.write(self.style.SUCCESS(f'Successfully'))