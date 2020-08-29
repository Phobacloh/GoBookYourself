from rest_framework import serializers
from .models import Project, Pledge

class ChoicesField(object):
    def __init__(self,choices):
        self.choices = choices
        # super(ChoicesField,self).__init__(**kwargs)

        # def to_representation(self,obj):
        #     return self._choices[obj]

        # def to_internal_value(self,data):
        #     return getattr(self._choices,data)

class PledgeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    amount = serializers.IntegerField()
    comment = serializers.CharField(max_length=500)
    anonymous = serializers.BooleanField()
    project_id = serializers.IntegerField()

    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)


class PledgeDetailSerializer(PledgeSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.amount = validated_data.get('amount', instance.amount)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.anonymous = validated_data.get('anonymous', instance.anonymous)
        instance.project_id = validated_data.get('project_id', instance.project_id)
        instance.save()
        return instance

class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=10000)
    goal = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    # owner = serializers.CharField(max_length=200)
    sample = serializers.CharField()
    pledges = PledgeSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.id')
    category = serializers.ChoiceField(choices=Project.CATEGORY_CHOICES)
   
    
    class Meta:
        model = Project
    
    # def get_category(self,obj):
    #     return obj.get_category_display()

    def create(self, validated_data):
        return Project.objects.create(**validated_data)
    
#**validated_data is compacting the dictionaries so you don't have to type it out individually like below:
        # title=validated_data.title, 
        
class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.sample = validated_data.get('sample', instance.sample)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance
