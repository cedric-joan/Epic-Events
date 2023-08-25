from typing import Any, Optional
from django.core.management.base import BaseCommand, CommandParser


class Command(BaseCommand):


    def add_arguments(self, parser: CommandParser):
        parser.add_argument("--name", type=str, help="le nom de l'utilisateur ne doit pas dépasser 30 caractères")

    def handle(self, *args: Any, **options: Any):
        name = options.get("name")
        self.stdout.write(self.style.SUCCESS(f"Hello world {name}"))
        
