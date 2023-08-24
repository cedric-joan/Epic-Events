from rest_framework.serializers import ModelSerializer
from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'password', 'confirm_password']

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            return f'Not matching password'
        return data

    def create(self, validate_data):
        user = User.objects.create(
            username=validate_data['username'], 
            email=validate_data['email'], 
            role=validate_data['role'])
        user.set_password(validate_data['password'])
        user.save()
        return user
    
    