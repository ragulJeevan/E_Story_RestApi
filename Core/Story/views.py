from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from django.db.models import Q
from my_Estory.Common.utils import api_response, api_error_response,api_paginated_response
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

class StoryPagination(PageNumberPagination):
    # Default values
    page_size = 10
    max_page_size = 1000

    def paginate_queryset(self, queryset, request, view=None):
        try:
            # Override to support `page` and `page_size` from request payload
            self.page = int(request.data.get('page', 1))  # Ensure page is an integer
            self.page_size = int(request.data.get('page_size', self.page_size))  # Ensure page_size is an integer
            if self.page_size <= 0:
                raise ValidationError("Page size must be greater than 0.")
            return super().paginate_queryset(queryset, request, view)
        except ValueError:
            raise ValidationError("Page and page_size must be valid integers.")

class StoryFilterPostAPI(APIView):
    pagination_class = StoryPagination

    def post(self, request, *args, **kwargs):
        try:
            # Extract filters from request body
            category_id = request.data.get('Category', None)
            created_by_id = request.data.get('created_by', None)
            header = request.data.get('header', None)
            page = request.data.get('page', 1)  # Default page is 1
            page_size = request.data.get('page_size', 10)  # Default page_size is 10
            # Validate page and page_size
            if not isinstance(page, int) or page <= 0:
                return api_error_response("Invalid page number. Must be a positive integer", status.HTTP_400_BAD_REQUEST)

            if not isinstance(page_size, int) or page_size <= 0:
                return api_error_response("Invalid page size. Must be a positive integer", status.HTTP_400_BAD_REQUEST)
            # Base queryset
            queryset = Story.objects.all()
            # Apply filters if provided
            if category_id:
                queryset = queryset.filter(Category=category_id)
            if created_by_id:
                queryset = queryset.filter(created_by=created_by_id)
            if header:
                queryset = queryset.filter(header__icontains=header)
            # Paginate the results
            paginator = StoryPagination()
            paginator.page_size = page_size
            paginated_queryset = paginator.paginate_queryset(queryset, request)
            # Serialize the data
            serializer = StorySerializer(paginated_queryset, many=True)
            # Return paginated response
            paginatorData = paginator.get_paginated_response(serializer.data).data
            return api_paginated_response(paginatorData, modelName,page,page_size)

        except ValidationError as e:
             return api_error_response(str(e), status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # Handle unexpected errors
            return api_error_response(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)