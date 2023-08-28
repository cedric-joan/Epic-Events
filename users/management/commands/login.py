from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class Command(BaseCommand):
    help = 'Log in to the application'

    def handle(self, *args, **kwargs ):
        username = input('username: ')
        password = input('password: ')

        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            token = Token.objects.get_or_create(user=user)
            self.stdout.write(self.style.SUCCESS(f'Logged in as {username}'))
            self.stdout.write(f'Your acces token is: {token.key}')
        else:
            self.stdout.write(self.style.ERROR('Authentication failed'))

        
