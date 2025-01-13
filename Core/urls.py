from django.urls import path
from .Category.views import CategoryList,CategoryDetail
from .Story.views import StoryList,StoryDetail

urlpatterns = [
    # CATEGORY 
      path('category_detail/', CategoryList.as_view(), name='category-list'),
      path('category_detail/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    # STORY     
      path('story_detail/', StoryList.as_view(), name='story-list'),
      path('story_detail/<int:pk>/', StoryDetail.as_view(), name='story-detail'),    
]