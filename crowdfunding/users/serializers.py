from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    profile_image = serializers.CharField(max_length=200)
    user_bio = serializers.CharField(max_length=200)
    username = serializers.CharField(max_length = 200)
    password = serializers.CharField(write_only=True)
    email = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
        