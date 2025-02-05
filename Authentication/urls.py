from django.urls import path
from .Views.Role import RoleList, RoleDetail,DeleteAllRoleView
from .Views.Routes import RoutesList, RoutesDetail,DeleteAllRouteView
from .Views.agreement import AgreementDetail,AgreementList,DeleteAllAgreementView
from .Views.State import StateList, StateDetail,DeleteAllStateView
from .Views.District import DistrictList, DistrictDetail,BulkDistrictCreateView,DeleteAllDistrictView
from .Views.Taluk import TaulkList, TaulkDetail,BulkTalukCreateView,DeleteAllTalukView
from .Views.Panchayat import PanchayatList, PanchayatDetail,BulkPanchayatCreateView,DeleteAllPanchayatView
from .Views.Users import UserProfileList, UserProfileDetail,UserProfileFilterPostAPI,UserProfileRandomRetrieveAPI,DeleteAllUsersView,CheckUserAPIView

urlpatterns = [
    # ROLE 
      path('role_detail/', RoleList.as_view(), name='role-list'),
      path('role_detail/<int:pk>/', RoleDetail.as_view(), name='role-detail'),
      path('delete_all_role/', DeleteAllRoleView.as_view(), name='delete-all-role'),
    # ROUTE     
      path('routes_detail/', RoutesList.as_view(), name='routes-list'),
      path('routes_detail/<int:pk>/', RoutesDetail.as_view(), name='routes-detail'), 
      path('delete_all_route/', DeleteAllRouteView.as_view(), name='all-route'), 
    # Agreement     
      path('agreement_detail/', AgreementList.as_view(), name='agreement-list'),
      path('agreement_detail/<int:pk>/', AgreementDetail.as_view(), name='agreement-detail'), 
      path('delete_all_agreement/', DeleteAllAgreementView.as_view(), name='all-agreement'),      
    # STATE 
      path('state_detail/', StateList.as_view(), name='state-list'),
      path('state_detail/<int:pk>/', StateDetail.as_view(), name='state-detail'),
      path('delete_all_state/', DeleteAllStateView.as_view(), name='all-state'),
    # DISTRICT 
      path('district_detail/', DistrictList.as_view(), name='district-list'),
      path('district_detail/<int:pk>/', DistrictDetail.as_view(), name='district-detail'),
      path('create_bulk_districts/', BulkDistrictCreateView.as_view(), name='bulk-district'),
      path('delete_all_district/', DeleteAllDistrictView.as_view(), name='all-district'),
    # TALUK 
      path('taluk_detail/', TaulkList.as_view(), name='taluk-list'),
      path('taluk_detail/<int:pk>/', TaulkDetail.as_view(), name='taluk-detail'),
      path('create_bulk_taluk/', BulkTalukCreateView.as_view(), name='bulk-taluk'),
      path('delete_all_taluk/', DeleteAllTalukView.as_view(), name='all-taluk'),
    # PANCHAYAT 
      path('panchayat_detail/', PanchayatList.as_view(), name='panchayat-list'),
      path('panchayat_detail/<int:pk>/', PanchayatDetail.as_view(), name='panchayat-detail'),
      path('create_bulk_panchayat/', BulkPanchayatCreateView.as_view(), name='bulk-panchayat'),
      path('delete_all_panchayat/', DeleteAllPanchayatView.as_view(), name='all-panchayat'),
    # EMPLOYEE
      # path('employee_detail/', EmployeeList.as_view(), name='employee-list'),
      # path('employee_detail/<int:pk>/', EmployeeDetail.as_view(), name='employee-detail'),
    # USER 
      path('user_detail/', UserProfileList.as_view(), name='user-list'),
      path('user_detail/<int:pk>/', UserProfileDetail.as_view(), name='user-detail'),
      path('user_filter/', UserProfileFilterPostAPI.as_view(), name='user-filter-post-api'),
      path('user_random/', UserProfileRandomRetrieveAPI.as_view(), name='user-random-post-api'),
      path('delete_all_user/', DeleteAllUsersView.as_view(), name='all-user'),
      path('check_user/', CheckUserAPIView.as_view(), name='all-user'),
]