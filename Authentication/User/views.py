from rest_framework.views import APIView
from rest_framework import status
from my_Estory.Common.utils import api_response, api_error_response,api_paginated_response,PaginationData
from ..models import UserProfile
from ..serializer import UserProfileSerializer
from django.http import Http404
from django.core.exceptions import ValidationError

modelName = "User"
notFound = "User not found"
ModelName = UserProfile
SerializerName = UserProfileSerializer

# LIST 
class UserProfileList(APIView):
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
# DETAIL 
class UserProfileDetail(APIView):
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
# PAGINATION 
class UserProfileFilterPostAPI(APIView):
    pagination_class = PaginationData

    def post(self, request, *args, **kwargs):
        try:
            # Extract filters from request body
            name = request.data.get('name', None)
            number = request.data.get('number', None)
            date_of_birth = request.data.get('date_of_birth', None)
            sex = request.data.get('sex', None)
            is_subscribed = request.data.get('is_subscribed', None)
            state = request.data.get('state', None)
            district = request.data.get('district', None)
            taluk = request.data.get('taluk', None)
            panchayat = request.data.get('panchayat', None)

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
            if name:
                queryset = queryset.filter(name=name)
            if number:
                queryset = queryset.filter(number=number)
            if date_of_birth:
                queryset = queryset.filter(date_of_birth__icontains=date_of_birth)
            if isinstance(is_subscribed, str):
                is_subscribed = is_subscribed.lower() == "true"
            if is_subscribed is not None:
                queryset = queryset.filter(is_subscribed=is_subscribed)
            if sex:
                queryset = queryset.filter(sex__icontains=sex)
            if state:
                queryset = queryset.filter(state__name__icontains=state)
            if district:
                queryset = queryset.filter(district__name__icontains=district)
            if taluk:
                queryset = queryset.filter(taluk__name__icontains=taluk)
            if panchayat:
                queryset = queryset.filter(panchayat__name__icontains=panchayat)
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
# RANDOM USER SELECTION 
class UserProfileRandomRetrieveAPI(APIView):
    def post(self, request, *args, **kwargs):
        try:
            # Extract the number of users to retrieve
            number = request.data.get('number', 10)  # Default to 10 if not provided
            state = request.data.get('state', None)
            district = request.data.get('district', None)
            taluk = request.data.get('taluk', None)
            panchayat = request.data.get('panchayat', None)
            date_of_birth = request.data.get('date_of_birth', None)
            is_subscribed = request.data.get('is_subscribed', None)
            # Base queryset
            queryset = UserProfile.objects.all()
            # Apply filters if provided
            if state:
                queryset = queryset.filter(state=state)
            if district:
                queryset = queryset.filter(district=district)
            if taluk:
                queryset = queryset.filter(taluk=taluk)
            if panchayat:
                queryset = queryset.filter(panchayat=panchayat)
            if date_of_birth:
                queryset = queryset.filter(date_of_birth=date_of_birth)
            if isinstance(is_subscribed, str):
                is_subscribed = is_subscribed.lower() == "true"
            if is_subscribed is not None:
                queryset = queryset.filter(is_subscribed=is_subscribed)
            # Get the total count of filtered users
            total_users = queryset.count()
            # If the requested number is greater than the total count, return all available users
            if number > total_users:
                number = total_users
            # Randomly shuffle the queryset and pick the requested number of users
            queryset = queryset.order_by('?')[:number]
            # Serialize the data
            serializer = UserProfileSerializer(queryset, many=True)
            # Return the response
            return api_response(serializer.data, modelName,'get')

        except Exception as e:
            # Return an error if something goes wrong
            return api_error_response([str(e)], status.HTTP_500_INTERNAL_SERVER_ERROR)