from django.urls import path
from .Views.category import CategoryList,CategoryDetail,DeleteAllCategoryView
from .Views.Story import StoryList,StoryDetail,StoryFilterPostAPI,GetStoriesByIds,DeleteAllStoryView
from .Views.StoryContent import StoryContentList,StoryContentDetail,DeleteAllStoryContentView,BulkCreateStoryContentAPIView

urlpatterns = [
    # CATEGORY 
      path('category_detail/', CategoryList.as_view(), name='category-list'),
      path('category_detail/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
      path('delete_all_category/', DeleteAllCategoryView.as_view(), name='delete-all-category'),
    # STORY     
      path('story_detail/', StoryList.as_view(), name='story-list'),
      path('story_detail/<int:pk>/', StoryDetail.as_view(), name='story-detail'),   
      path('story_filter/', StoryFilterPostAPI.as_view(), name='story-filter-post-api'),
      path('stories-by-ids/', GetStoriesByIds.as_view(), name='stories-by-ids'),
      path('delete_all_story/', DeleteAllStoryView.as_view(), name='delete-all-story'),
    # STORY CONTENT 
      path('story_content_detail/', StoryContentList.as_view(), name='story-content-list'),
      path('story_content_detail/<int:pk>/', StoryContentDetail.as_view(), name='story-content-detail'),
      path('delete_all_story_content/', DeleteAllStoryContentView.as_view(), name='delete-all-story-content'),
      path('bulk_add_stories/', BulkCreateStoryContentAPIView.as_view(), name='bulk-add-stories'),
]