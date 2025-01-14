from django.urls import path
from .Role.views import RoleList, RoleDetail
from .Routes.views import RoutesList, RoutesDetail
from .State.views import StateList, StateDetail
from .District.views import DistrictList, DistrictDetail
from .Taluk.views import TaulkList, TaulkDetail
from .Panchayat.views import PanchayatList, PanchayatDetail
from .Employee.views import EmployeeList, EmployeeDetail
from .User.views import UserProfileList, UserProfileDetail,UserProfileFilterPostAPI,UserProfileRandomRetrieveAPI

urlpatterns = [
    # ROLE 
      path('role_detail/', RoleList.as_view(), name='role-list'),
      path('role_detail/<int:pk>/', RoleDetail.as_view(), name='role-detail'),
    # ROUTE     
      path('routes_detail/', RoutesList.as_view(), name='routes-list'),
      path('routes_detail/<int:pk>/', RoutesDetail.as_view(), name='routes-detail'),    
    # STATE 
      path('state_detail/', StateList.as_view(), name='state-list'),
      path('state_detail/<int:pk>/', StateDetail.as_view(), name='state-detail'),
    # DISTRICT 
      path('district_detail/', DistrictList.as_view(), name='district-list'),
      path('district_detail/<int:pk>/', DistrictDetail.as_view(), name='district-detail'),
    # TALUK 
      path('taluk_detail/', TaulkList.as_view(), name='taluk-list'),
      path('taluk_detail/<int:pk>/', TaulkDetail.as_view(), name='taluk-detail'),
    # PANCHAYAT 
      path('panchayat_detail/', PanchayatList.as_view(), name='panchayat-list'),
      path('panchayat_detail/<int:pk>/', PanchayatDetail.as_view(), name='panchayat-detail'),
    # EMPLOYEE
      path('employee_detail/', EmployeeList.as_view(), name='employee-list'),
      path('employee_detail/<int:pk>/', EmployeeDetail.as_view(), name='employee-detail'),
    # USER 
      path('user_detail/', UserProfileList.as_view(), name='user-list'),
      path('user_detail/<int:pk>/', UserProfileDetail.as_view(), name='user-detail'),
      path('user_filter/', UserProfileFilterPostAPI.as_view(), name='user-filter-post-api'),
      path('user_random/', UserProfileRandomRetrieveAPI.as_view(), name='user-random-post-api'),
]