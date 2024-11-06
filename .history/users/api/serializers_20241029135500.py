from rest_framework import serializers
from users.models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['id', 'email', 'username', 'password']
        
    #override del metodo crear usuarios
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        
        instance.save()
        return instance
    
        #hacemos pip install djangorestframework-jwt
        
        
#nuevo serializador para consulta
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser']
        
#* serializador para actualizar los datos del usuario
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
        read_only_fields = ['id', 'is_active', 'is_staff', 'is_superuser']
        
    # #metodo para actualizar los datos
    # def update(self, instance, validated_data):
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.username = validated_data.get('username', instance.username)
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.last_name = validated_data.get('last_name', instance.last_name)
        
    #     instance.save()
    #     return instance