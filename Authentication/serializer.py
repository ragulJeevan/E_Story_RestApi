from rest_framework import serializers
from .models import Role,Employee,State,District,Taluk,Panchayat,UserProfile,Route

# ROLE SERIALIZER 
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name', 'routes']


# EMPLOYEE SERIALIZER
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


# STATE SERIALIZER
class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

# DISTRICT SERIALIZER
class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['name', 'created_at', 'updated_at']


# BULK SERIALIZER
class BulkDistrictCreateSerializer(serializers.Serializer):
    state_id = serializers.IntegerField()
    districts = serializers.ListSerializer(
        child=serializers.DictField(child=serializers.CharField(max_length=255))
    )

    def validate_state_id(self, value):
        try:
            state = State.objects.get(id=value)
            return state
        except State.DoesNotExist:
            raise serializers.ValidationError("State with the given ID does not exist.")

    def create(self, validated_data):
        state = validated_data['state_id']
        districts_data = validated_data['districts']
        districts = [District(name=d['name'], state=state) for d in districts_data]
        created_districts = District.objects.bulk_create(districts)
        return created_districts


# TALUK SERIALIZER
class TalukSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taluk
        fields = ['name', 'created_at', 'updated_at']


#  BULK TALUK SERIALIZER       
class BulkTalukCreateSerializer(serializers.Serializer):
    district_id = serializers.IntegerField()
    taluk = serializers.ListSerializer(
        child=serializers.DictField(child=serializers.CharField(max_length=255))
    )

    def validate_district_id(self, value):
        try:
            district = District.objects.get(id=value)
            return district
        except District.DoesNotExist:
            raise serializers.ValidationError("District with the given ID does not exist.")

    def create(self, validated_data):
        district = validated_data['district_id']
        taluk_data = validated_data['taluk']
        taluks = [Taluk(name=t['name'], district=district) for t in taluk_data]
        created_taluks = Taluk.objects.bulk_create(taluks)
        return created_taluks

# PANCHAYAT SERIALIZER
class PanchayatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Panchayat
        fields = ['name', 'created_at', 'updated_at']

# BULK PANCHAYAT SERIALIZER        
class BulkPanchayatCreateSerializer(serializers.Serializer):
    taluk_id = serializers.IntegerField()
    panchayat = serializers.ListSerializer(
        child=serializers.DictField(child=serializers.CharField(max_length=255))
    )

    def validate_taluk_id(self, value):
        try:
            taluk = Taluk.objects.get(id=value)
            return taluk
        except Taluk.DoesNotExist:
            raise serializers.ValidationError("Taluk with the given ID does not exist.")

    def create(self, validated_data):
        taluk = validated_data['taluk_id']
        panchayats_data = validated_data['panchayat']
        panchayats = [Panchayat(name=p['name'], taluk=taluk) for p in panchayats_data]
        created_panchayats = Panchayat.objects.bulk_create(panchayats)
        return created_panchayats

# USER SERIALIZER
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

# ROUTE SERIALIZER
class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'