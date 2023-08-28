from django.core.management.base import BaseCommand
from users.models import User

class Command(BaseCommand):
    help = 'Create a new user'

    def add_arguments(self, parser) :
        parser.add_argument('--username', type=str, help="username must not exceed 30 characters")
        parser.add_argument('--email', type=str, help="email must not exceed 30 characters")
        parser.add_argument('--password', type=str, help="password must not exceed 30 characters")
        parser.add_argument('--role', type=str, help="role must be in list [MGT, SAL, SUP]")

    def handle(self, *args, **options):
        username = options.get('username')
        email = options.get('email')
        password = options.get('password')
        role = options.get('role')
        
        User.objects.create(username=username, email=email, password=password, role=role)
        self.stdout.write(self.style.SUCCESS(f'User created successfully'))