from django.db import models
from django.contrib.auth.models import User

ROLE_CHOICES = (
    ('MANAGEMENT', 'Management'),
    ('SALES', 'Sales'),
    ('SUPPORT', 'Support')
)


class UserManager(models.Model):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=25)
    password = models.CharField(max_length=20)
    confirm_password = models.CharField(max_length=20)
    role = models.CharField(choices=ROLE_CHOICES, null=False)



    def validate(self, data):
        if data['password'] != data['confirm_password']:
            return f'Not matching password'
        return data

    def create(self, validate_data):
        user = User.objects.create(username=validate_data['username'], email=validate_data['email'])
        user.set_password(validate_data['password'])
        user.save()
        return user
        
    def __str__(self):
        return f"{self.username} - {self.role}"
