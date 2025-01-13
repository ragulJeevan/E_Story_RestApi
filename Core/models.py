from django.db import models
from django.core.validators import MaxLengthValidator
from Authentication.models import Employee

class Category(models.Model):
    name=models.CharField(max_length=255)
    created_by=models.ForeignKey(Employee,on_delete=models.SET_NULL,null=True,related_name="category_created")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_by=models.ForeignKey(Employee,on_delete=models.SET_NULL,null=True,related_name="category_updated")
    updated_at=models.DateTimeField(auto_now=True)

class Story(models.Model):
    header=models.CharField(max_length=255)
    sub_header=models.CharField(max_length=255)
    line_up=models.TextField(validators=[MaxLengthValidator(1000)])
    Category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,related_name="story_category")
    display_image=models.ImageField(upload_to="story-images/",blank=True,null=True)
    created_by=models.ForeignKey(Employee,on_delete=models.SET_NULL,null=True,related_name="story_created")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_by=models.ForeignKey(Employee,on_delete=models.SET_NULL,null=True,related_name="story_updated")
    updated_at=models.DateTimeField(auto_now=True)