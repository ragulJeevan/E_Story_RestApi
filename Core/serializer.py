from rest_framework import serializers
from .models import Category,Story


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Story
        fields ='__all__'