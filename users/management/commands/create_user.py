from django.core.management.base import BaseCommand
from users.models import User

class Command(BaseCommand):
    help = 'Create a new user'

    def add_arguments(self, parser) :
        parser.add_argument('--username', type=str)
        parser.add_argument('--email', type=str)
        parser.add_argument('--password', type=str)
        parser.add_argument('--role', type=str)

    def handle(self, *args, **options):
        username = options['username']
        email = options['email']
        password = options['password']
        role = options['role']
        
        User.objects.create(username=username, email=email, password=password, role=role)
        self.stdout.write(self.style.SUCCESS(f'User created successfully'))