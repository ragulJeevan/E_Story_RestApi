from rest_framework import status
from rest_framework.response import Response

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
        "message": model + "data provided successfully",
        "count":len(data),
        "pageNumber":pageNumber,
        "page_size":page_size,
        "data": data
    }, status=status_code)