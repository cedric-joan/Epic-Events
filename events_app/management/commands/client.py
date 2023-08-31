from django.core.management.base import BaseCommand
from .clients import menu, controllers

class Command(BaseCommand):
    help = 'Menu client'

    def handle(self, *args, **options):
        choise = menu()
        controllers(choise)
        self.stdout.write(self.style.SUCCESS("Successfully"))