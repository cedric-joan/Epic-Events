from rest_framework.serializers import ModelSerializer
from .models import User


class SignupSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'password', 'confirm_password']

    
    
class EmployeeSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name','role']