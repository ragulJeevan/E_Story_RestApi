from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from my_Estory.Common.utils import api_response, api_error_response,api_paginated_response,PaginationData
from ..models import Story
from ..serializer import StorySerializer
from django.http import Http404
from django.core.exceptions import ValidationError

modelName = "Story"
notFound = "Story not found"
ModelName = Story
SerializerName = StorySerializer


class StoryList(APIView):
    def get(self, request):
         try:
             requestData = ModelName.objects.all()
             serializer = SerializerName(requestData, many=True)
             return api_response(serializer.data, modelName, 'get')
         except Exception as e:
             return api_error_response([str(e)], status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):   
        try:
            serializer = SerializerName(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return api_response(serializer.data, modelName, 'save')
            return api_error_response(serializer.errors)
        except Exception as e:
            return api_error_response([str(e)], status.HTTP_500_INTERNAL_SERVER_ERROR)

class StoryDetail(APIView):
    def get_object(self, pk):
        try:
            return ModelName.objects.get(pk=pk)
        except ModelName.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        try:
            requestData = self.get_object(pk)
            serializer = SerializerName(requestData)
            return api_response(serializer.data, modelName, 'get')
        except Http404:
            return api_error_response([notFound], status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return api_error_response([str(e)], status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            requestData = self.get_object(pk)
            serializer = SerializerName(requestData, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return api_response(serializer.data, modelName, 'update')
            return api_error_response(serializer.errors)
        except Http404:
            return api_error_response([notFound], status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return api_error_response([str(e)], status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            requestData = self.get_object(pk)
            requestData.delete()
            return api_response('', modelName, 'delete')
        except Http404:
            return api_error_response([notFound], status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return api_error_response([str(e)], status.HTTP_500_INTERNAL_SERVER_ERROR)


class StoryFilterPostAPI(APIView):
    pagination_class = PaginationData

    def post(self, request, *args, **kwargs):
        try:
            # Extract filters from request body
            category_id = request.data.get('Category', None)
            created_by_id = request.data.get('created_by', None)
            title = request.data.get('title', None)
            is_reviewed = request.data.get('is_reviewed', None)
            is_published = request.data.get('is_published', None)

            page = request.data.get('page', 1)  # Default page is 1
            page_size = request.data.get('page_size', 10)  # Default page_size is 10
            # Validate page and page_size
            if not isinstance(page, int) or page <= 0:
                return api_error_response("Invalid page number. Must be a positive integer", status.HTTP_400_BAD_REQUEST)

            if not isinstance(page_size, int) or page_size <= 0:
                return api_error_response("Invalid page size. Must be a positive integer", status.HTTP_400_BAD_REQUEST)
            # Base queryset
            queryset = ModelName.objects.all()
            # Apply filters if provided
            if category_id:
                queryset = queryset.filter(Category=category_id)
            if created_by_id:
                queryset = queryset.filter(created_by=created_by_id)
            if title:
                queryset = queryset.filter(title__icontains=title)
            if isinstance(is_reviewed, str):
                is_reviewed = is_reviewed.lower() == "true"
            if is_reviewed is not None:
                queryset = queryset.filter(is_reviewed=is_reviewed)
            if isinstance(is_published, str):
                is_published = is_published.lower() == "true"
            if is_published is not None:
                queryset = queryset.filter(is_published=is_published)
            # Paginate the results
            paginator = PaginationData()
            paginator.page_size = page_size
            paginated_queryset = paginator.paginate_queryset(queryset, request)
            # Serialize the data
            serializer = SerializerName(paginated_queryset, many=True)
            # Return paginated response
            paginatorData = paginator.get_paginated_response(serializer.data).data
            return api_paginated_response(paginatorData, modelName,page,page_size)

        except ValidationError as e:
             return api_error_response(str(e), status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # Handle unexpected errors
            return api_error_response(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetStoriesByIds(APIView):
    def post(self, request):
        # Extract IDs from the request payload
        ids = request.data.get('id', [])
        
        if not ids or not isinstance(ids, list):
            return api_error_response({'Null Error'}, status.HTTP_400_BAD_REQUEST,'No Recent Stories')
        
        # Fetch stories by IDs
        stories = Story.objects.filter(id__in=ids)
        serializer = StorySerializer(stories, many=True)
        return api_response(serializer.data, modelName, 'get')

class DeleteAllStoryView(APIView):
    def delete(self, request):
        # Get all roles to show what is being deleted (optional)
        roles_to_delete = list(ModelName.objects.values('id', 'name'))
        
        # Delete all roles
        deleted_count, _ = ModelName.objects.all().delete()
        return Response(
            {
                "message": "All stories have been deleted successfully.",
                "deleted_roles": roles_to_delete,
                "total_deleted": deleted_count,
            },
            status=status.HTTP_200_OK
        )
