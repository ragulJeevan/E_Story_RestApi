from django.db import models
from django.core.validators import MaxLengthValidator
from Authentication.models import UserProfile

class Category(models.Model):
    name=models.CharField(max_length=255)
    created_by=models.ForeignKey(UserProfile,on_delete=models.SET_NULL,null=True,related_name="category_created")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_by=models.ForeignKey(UserProfile,on_delete=models.SET_NULL,null=True,related_name="category_updated")
    updated_at=models.DateTimeField(auto_now=True)

class Story(models.Model):
    title=models.CharField(max_length=255)
    Category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,related_name="story_category")
    display_image=models.ImageField(upload_to="story-images/",blank=True,null=True)
    is_reviewed = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    created_by=models.ForeignKey(UserProfile,on_delete=models.SET_NULL,null=True,related_name="story_created")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_by=models.ForeignKey(UserProfile,on_delete=models.SET_NULL,null=True,related_name="story_updated")
    updated_at=models.DateTimeField(auto_now=True)

class StoryContent(models.Model):
    title = models.CharField(max_length=255)
    content=models.TextField(validators=[MaxLengthValidator(1000)])
    story_id=models.ForeignKey(Story,on_delete=models.CASCADE,related_name='story_id')
    created_by=models.ForeignKey(UserProfile,on_delete=models.SET_NULL,null=True,related_name="story_content_created")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_by=models.ForeignKey(UserProfile,on_delete=models.SET_NULL,null=True,related_name="story_content_updated")
    updated_at=models.DateTimeField(auto_now=True)