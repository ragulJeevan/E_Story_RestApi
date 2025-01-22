from rest_framework import serializers
from .models import Category,Story,StoryContent


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class StoryContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryContent
        fields = ['id', 'title', 'content', 'story_id', 'created_by', 'created_at', 'updated_at', 'updated_by']

class StorySerializer(serializers.ModelSerializer):
    story_id = StoryContentSerializer(many=True, read_only=True)  # Related name for StoryContent
    
    class Meta:
        model = Story
        fields = [
            'id', 
            'title', 
            'Category', 
            'display_image', 
            'is_reviewed', 
            'is_published', 
            'created_by', 
            'created_at', 
            'updated_by', 
            'updated_at', 
            'story_id' 
        ]

