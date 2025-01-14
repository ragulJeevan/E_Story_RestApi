from django.db import models
import uuid

class Role(models.Model):
    name = models.CharField(max_length=255)
    routes = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=255)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, related_name='employee')
    number = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='states_created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='states_updated')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='districts')
    created_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='districts_created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='districts_updated')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Taluk(models.Model):
    name = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='taluks')
    created_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='taluks_created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='taluks_updated')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Panchayat(models.Model):
    name = models.CharField(max_length=255)
    taluk = models.ForeignKey(Taluk, on_delete=models.CASCADE, related_name='panchayats')
    created_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='panchayats_created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='panchayats_updated')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    name = models.CharField(max_length=255)
    user_uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    number = models.CharField(max_length=15, unique=True)
    whatsapp_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField()
    sex = models.CharField(max_length=10, choices=(('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')))
    is_subscribed = models.BooleanField(default=False)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, related_name='users')
    display_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, related_name='users')
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, related_name='users')
    taluk = models.ForeignKey(Taluk, on_delete=models.SET_NULL, null=True, related_name='users')
    panchayat = models.ForeignKey(Panchayat, on_delete=models.SET_NULL, null=True, related_name='users')
    address = models.TextField()
    pincode = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Route(models.Model):
    route_name = models.CharField(max_length=255)
    route_image = models.CharField(max_length=255, blank=True, null=True)  # Store the image URL as a string
    route_url = models.CharField(max_length=255)  # URL field for the route's web link
    is_main = models.BooleanField(default=False)
    created_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='routes_created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='routes_updated')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.route_name
