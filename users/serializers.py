from rest_framework.serializers import ModelSerializer
from .models import User


class SignupSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'password', 'confirm_password']

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
        # user.set_password(validate_data['password'])
        if user.role in ['MGT', 'SAL', 'SUP']:
            user.is_staff = True
            user.save()
        return user
    
class EmployeeSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name','role']