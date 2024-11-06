from rest_framework import serializers
from users.models import User

class User RegisterSerializer (serializers. ModelSerializer):
    model= User
    fields = ['id', 'email', 'username', 'password']