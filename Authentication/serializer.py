from rest_framework import serializers
from .models import Role,Employee,State,District,Taluk,Panchayat,UserProfile,Route


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name', 'routes']

class EmployeeSerializer(serializers.ModelSerializer):
    role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all())  # Accept role as ID for POST and PUT
    
    class Meta:
        model = Employee
        fields = '__all__'

    def to_representation(self, instance):
        """ Override this method to customize the way the data is returned. """
        representation = super().to_representation(instance)
        # Use RoleSerializer to return nested role data on GET
        representation['role'] = RoleSerializer(instance.role).data
        return representation

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

# class UserProfileSerializer(serializers.ModelSerializer):
#     role = RoleSerializer()
#     class Meta:
#         model = UserProfile
#         fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all())  # Accept role as ID for POST and PUT
    
    class Meta:
        model = UserProfile
        fields = '__all__'

    def to_representation(self, instance):
        """ Override this method to customize the way the data is returned. """
        representation = super().to_representation(instance)
        # Use RoleSerializer to return nested role data on GET
        representation['role'] = RoleSerializer(instance.role).data
        return representation

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'