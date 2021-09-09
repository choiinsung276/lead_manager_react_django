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
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        # 유저네임, 패스워드 맞는지 일일이 구현하는게 아니라 장고에서 구현해놓음
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
