from rest_framework import serializers
from users.models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    model= User
    fields = ['id', 'email', 'username', 'password']