from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    profile_image = serializers.CharField(max_length=200)
    user_bio = serializers.CharField(max_length=200)
    country = serializers.CharField(max_length = 200)
    username = serializers.CharField(max_length = 200)
    password = serializers.CharField(write_only=True)
    email = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class CustomUserDetailsSerializer(CustomUserSerializer):
    def update(self, instance, validated_data):
        # print('vd', validated_data)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.profile_image = validated_data.get('profile_image', instance.profile_image)
        instance.user_bio = validated_data.get('user_bio', instance.user_bio)
        instance.country = validated_data.get('country', instance.country)
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        # print('instance', instance)
        return instance


        