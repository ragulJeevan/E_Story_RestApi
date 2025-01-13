from rest_framework import serializers
from .models import Role,Employee,State,District,Taluk,Panchayat,UserProfile,Route


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'

class TalukSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taluk
        fields = '__all__'

class PanchayatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Panchayat
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'