from django.core.management.base import BaseCommand
from .contracts import menu, controllers

class Command(BaseCommand):
    help = 'Menu contract'

    def handle(self, *args, **options):
        
        choise = menu()
        controllers(choise)
        self.stdout.write(self.style.SUCCESS("Successfully"))