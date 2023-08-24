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



    def __str__(self):
        return f"{self.username} - {self.role}"