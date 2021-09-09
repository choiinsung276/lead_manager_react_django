from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# 장고에서 User 모델 제공해줌 token을 위해 knox를 사용한다.
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password':{'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],validated_data['password'])

        return user

# Login Serializer