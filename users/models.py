from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    ROLE_CHOICES = (
        ('MGT', 'Management'),
        ('SAL', 'Sales'),
        ('SUP', 'Support')
    )

    username = models.CharField(unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField()
    confirm_password = models.CharField()
    role = models.CharField(choices=ROLE_CHOICES, null=False)

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            return f'Not matching password'
        return data

    def create(self, validate_data):
        user = User.objects.create(
            username=validate_data['username'], 
            email=validate_data['email'], 
            role=validate_data['role'],
            password=validate_data['password'])
        user.set_password(validate_data['password'])
        user.save()
        return user

    def __str__(self):
        return f"{self.username} - {self.role}"