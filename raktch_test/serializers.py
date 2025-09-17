from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ['email', 'password', 'password2']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords must match."})
        validate_password(attrs['password'])
        return attrs

    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']

        user = User.objects.create_user(username=email, email=email, password=password)
        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = "email" 

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        if email is None or password is None:
            raise serializers.ValidationError("Email and password required")

        user = authenticate(username=email, password=password)
        if user is None:
            raise serializers.ValidationError("No active account found with the given credentials")

    
        data = super().validate({"username": user.username, "password": password})
        return data
