from rest_framework import serializers
from .models import CustomUser


class ChoicesField(object):
    def __init__(self,choices):
        self.choices = choices


class CustomUserSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(write_only=True)
    email = serializers.CharField(max_length=200)
    tagline = serializers.CharField(max_length=200, required = False)
    bio = serializers.CharField(required=False)
    profile_pic = serializers.URLField(required=False)
    favorite_genre = serializers.ChoiceField(required=False, choices=CustomUser.CATEGORY_CHOICES)
   
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.tagline = validated_data.get('tagline', instance.tagline)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.profile_pic = validated_data.get('profile_pic', instance.profile_pic)
        instance.favorite_genre = validated_data.get('favorite_genre', instance.favorite_genre)
        instance.save()
        return instance

    class Meta:
        model = CustomUser
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    # def create (self, validated_data):
    #     return CustomUser.objects.create(**validated_data)
    
    


        