from rest_framework import status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.core.exceptions import ValidationError

# RESPONSE SUCCESS 
def api_response(data,model, operation, status_code=status.HTTP_200_OK):
    
    if operation == 'get':
        message = model + " provided successfully"
    elif operation == 'save':
        message = model + " added successfully"
    elif operation == 'update':
        message = model + " updated successfully"
    elif operation == 'delete':
        message = model + " deleted successfully"
    elif operation == 'login':
        message = 'Loggedn in successfully'
    else:
        message = "Operation successful"
    
    return Response({
        "status": True,
        "status_code": status_code,
        "message": message,
        "data": data
    }, status=status_code)


# ERROR RESPONSE 
def api_error_response(data,status_code=status.HTTP_400_BAD_REQUEST):
    
    return Response({
        "status": False,
        "status_code": status_code,
        "message": 'Something went wrong. Try again later !!!',
        "error": data
    }, status=status_code)

# PAGINATED RESPONSE 
def api_paginated_response(data,model,pageNumber,page_size,status_code=status.HTTP_200_OK):
       return Response({
        "status": True,
        "status_code": status_code,
        "message": f"{str(model)} data provided successfully",
        "total_data":data.get('count', 0),
        "pageNumber":pageNumber,
        "page_size":page_size,
        "data": data.get('results', [])
    }, status=status_code)

class PaginationData(PageNumberPagination):
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