from rest_framework import serializers
from .models import User,ContactUs
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['phone','country', 'email', 'first_name', 'last_name', 'password','howDidYouFindUs']

    def create(self, validated_data):
        user = User.objects.create(
             phone=validated_data['phone'],
             country=validated_data['country'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password'],
             howDidYouFindUs=validated_data['howDidYouFindUs']
            
        )
        return user
    
class ContactUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactUs
        fields = ['phone','fullName', 'email', 'message']

    def create(self, validated_data):
        contactus = ContactUs.objects.create(
             phone=validated_data['phone'],
             fullName=validated_data['fullName'],
            email=validated_data['email'],
            message=validated_data['message']
            
        )
        return contactus

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()