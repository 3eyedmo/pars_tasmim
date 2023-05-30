from rest_framework import serializers
from django.contrib.auth import get_user_model

from accounts.utils import password_validation



class ReadOnlyUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(read_only=True)


class BaseUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()

class UserRegisterSerializer(BaseUserSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)


    def validate_password2(self, password2):
        password1 = self.initial_data.get("password1")
        is_valid, message = password_validation(password1, password2)
        if not is_valid:
            raise serializers.ValidationError(message)
        return password2
    
    def validate_email(self, email):
        if get_user_model().objects.filter(email=email).exists():
            raise serializers.ValidationError({
                "email": "email exists!"
            })
        return email
    
    def create(self, validated_data):
        email = validated_data.get("email")
        password = validated_data.get("password2")
        User = get_user_model()
        user = User(email=email)
        user.set_password(password)
        user.save()
        return user


