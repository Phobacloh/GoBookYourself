from rest_framework import serializers
from .models import Project, Pledge

class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=10000)
    goal = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    owner = serializers.CharField(max_length=200)
    sample = serializers.CharField(max_length=10000)

    def create(self, validated_data):
        return Project.objects.create(**validated_data)
    
class PledgeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    amount = serializers.IntegerField()
    comment = serializers.CharField(max_length 500)
    anonymous = serializers.BooleanField()
    project_id = serializers.IntegerField()

    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)