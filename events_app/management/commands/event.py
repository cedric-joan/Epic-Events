from django.core.management.base import BaseCommand
from .events import menu, controllers

class Command(BaseCommand):
    help = 'Menu event'

    def handle(self, *args, **options):
        choise = menu()
        controllers(choise)
        self.stdout.write(self.style.SUCCESS("Successfully"))